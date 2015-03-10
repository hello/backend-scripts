#!/usr/bin/python

import requests
import json
import sys
import sys
import argparse


parser = argparse.ArgumentParser(description="Returns a list of seen devices for a given firmware version. ")
parser.add_argument('--env', choices=['local','dev','prod'], default='local', help='Environment')
parser.add_argument('-e','--endpoint', help='API endpoint override')
parser.add_argument('-t','--token', help='OAuth Token')
parser.add_argument('-f','--firmware_version', help='Firmware Version (dec)')
parser.add_argument('-fh','--firmware_version_hex', help='Firmware Version (hex)')
parser.add_argument('-v','--verbose', action='store_true', help='Verbose output')
args = parser.parse_args()


FW_VERSION = 0
if args.firmware_version_hex != None:
  FW_VERSION = int(args.firmware_version_hex, 16)
elif args.firmware_version != None:
  FW_VERSION = int(args.firmware_version)

if args.endpoint != None:
	ENDPOINT = args.endpoint
elif args.env == 'prod':
  print "You probably shouldn't be querying Prod. Edit this script if you really know what you're doing. "
  ENDPOINT = "http://localhost:9999/v1/"
elif args.env == 'dev':
	ENDPOINT = "https://dev-api.hello.is/v1/"
elif args.env == 'local':
	ENDPOINT = "http://localhost:9999/v1/"


PATH = 'firmware/devices/'

# Define data and header payload
headers = {
  'Content-Type' : 'application/json', 
  'Authorization' : 'Bearer %s' % args.token
}

payload = {
  'firmware_version': FW_VERSION
}

if args.verbose:
  print "*" * 10
  print "Contacting: " + ENDPOINT
  print "Getting Devices Seen With Firmware: " + str(FW_VERSION) + " (" + str(hex(FW_VERSION)) + ")"
  print "*" * 10

while True:
  resp = requests.get(ENDPOINT + PATH, headers=headers, params=payload)

  if resp.status_code != 200:
  	print "Error contacting server."
  	sys.exit(resp.content)
  
  if args.verbose:
    print "Server response:"

  print json.loads(resp.content)

  break;
