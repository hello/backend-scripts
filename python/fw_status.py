#!/usr/bin/python

import requests
import json
import sys
import argparse
import time
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

parser = argparse.ArgumentParser(description="Returns the number of seen devices on a given firmware version. ")
parser.add_argument('--env', choices=['local','dev','prod'], default='local', help='Environment')
parser.add_argument('-e','--endpoint', help='API endpoint override')
parser.add_argument('-t','--token', help='OAuth Token')
parser.add_argument('-f','--firmware_version', help='Firmware Version (dec)')
parser.add_argument('-fh','--firmware_version_hex', help='Firmware Version (hex)')
parser.add_argument('-v','--verbose', action='store_true', help='Verbose output')
parser.add_argument('-d','--duration', help='Duration of window')
parser.add_argument('-a','--all', action='store_true', help='Print all seen fw versions')
parser.add_argument('-s','--slack', action='store_true', help='Send to Slack')
args = parser.parse_args()


FW_VERSION = 0
if args.firmware_version_hex != None:
    FW_VERSION = int(args.firmware_version_hex, 16)
elif args.firmware_version != None:
    FW_VERSION = int(args.firmware_version)

if args.endpoint != None:
    ENDPOINT = args.endpoint
elif args.env == 'prod':
    ENDPOINT = "https://admin-api.hello.is/v1/"
elif args.env == 'dev':
    ENDPOINT = "https://dev-api.hello.is/v1/"
elif args.env == 'local':
    ENDPOINT = "http://localhost:9999/v1/"

DURATION_IN_MINS = 5
if args.duration != None:
    DURATION_IN_MINS = args.duration


LIST_PATH = 'firmware/list_by_time/'


# Define data and header payload
headers = {
    'Content-Type' : 'application/json',
    'Authorization' : 'Bearer %s' % args.token
}

nowTimestamp = int(time.time() * 1000)

payload = {
    'range_start': nowTimestamp - (int(DURATION_IN_MINS) * 60000),
    'range_end': nowTimestamp + 60000 #add a minute just to make sure I'm catching every device
}

def getFWName(s):
    NAME_PATH = 'firmware/names/'
    while True:
        resp = requests.get(ENDPOINT + NAME_PATH + s, headers=headers)

        if resp.status_code != 200:
            print "Error contacting server while fetching FW name."
            sys.exit(resp.content)

        if args.verbose:
            print "Server response:"

        versionResp = json.loads(resp.content)
        if len(versionResp) > 0:
            return versionResp[0]
        else:
            return "Unknown"
        break

SLACK_MESSAGE = ""

while True:
    resp = requests.get(ENDPOINT + LIST_PATH, headers=headers, params=payload)

    if resp.status_code != 200:
        print "Error contacting server."
        sys.exit(resp.content)

    if args.verbose:
        print "Server response:"


    totalCount = 0
    for seenFirmware in json.loads(resp.content):
        totalCount += seenFirmware["count"]

    allSeenFW = json.loads(resp.content)
    for seenFirmware in sorted(allSeenFW, reverse=True):
        if (int(seenFirmware["version"]) == int(FW_VERSION)) or (args.all == True):
            versionName = getFWName(str(hex(int(seenFirmware["version"]))[2:]))
            versionNamePadding = 18
            if args.slack == True:
                versionNamePadding += 62 + len(str(seenFirmware["version"]))
                versionName = "<https://hello-admin.appspot.com/firmware/?firmware_version=" + str(seenFirmware["version"]) + "|" + versionName + ">"

            SLACK_MESSAGE += versionName.ljust(versionNamePadding) + " (" + str(seenFirmware["version"]).ljust(10) + " | " + str(hex(int(seenFirmware["version"]))[2:]).ljust(8) + ") seen on " + str(seenFirmware["count"]).rjust(6) + "/" + str(totalCount) + " (" + str(float(seenFirmware["count"])/float(totalCount) * 100.0)[:5] + "%) devices in the past " + str(DURATION_IN_MINS) + "mins\n"

    break


if args.slack == True:
    SLACK_ENDPOINT = "https://hooks.slack.com/services/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"
    slackPayload = {
        "username": "FW Rollout Bot",
        "icon_emoji": ":traffic_light:",
        "text": "Current FW Info:\n```" + SLACK_MESSAGE + "```"
    }

    while True:
        resp = requests.put(SLACK_ENDPOINT, json=slackPayload)

        if resp.status_code != 200:
            print "Error contacting server."
            sys.exit(resp.content)

        break
else:
    print SLACK_MESSAGE


