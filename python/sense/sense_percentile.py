#!/usr/bin/python

import argparse
from decimal import Decimal

parser = argparse.ArgumentParser(description="Returns the percentile rank for a given Sense ID. ")
parser.add_argument('-i', '--device_id', help='Sense ID')
args = parser.parse_args()

if args.device_id != None:
    deviceId = args.device_id
else:
    deviceId = ""

def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

hash = (Decimal(abs(java_string_hashcode(deviceId))) % (Decimal(100.0) * Decimal(100.0)) / Decimal(100.0))
print hash
