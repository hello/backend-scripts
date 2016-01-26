import requests
import sys
import time
import sys
import signing
import ntp_pb2

ENDPOINT = "http://127.0.0.1:1111/"

print ENDPOINT 

DEVICE_ID = "fake-sense"
AES_KEY = "0C95235EDF61C28FDDF5971C148BA9A2"

#DEVICE_ID = "0000000000000000"
#AES_KEY = "31323334353637383931323334353637" #default key



# Reference Timestamp: Time when the system clock was last set or
# corrected, in NTP timestamp format.
#
# Origin Timestamp (org): Time at the client when the request departed
# for the server, in NTP timestamp format.
#
# Receive Timestamp (rec): Time at the server when the request arrived
# from the client, in NTP timestamp format.
#
# Transmit Timestamp (xmt): Time at the server when the response left
# for the client, in NTP timestamp format.
timePacket = ntp_pb2.NTPDataPacket()
timePacket.reference_ts = 1053843538
timePacket.origin_ts = 1453843538

pb_string = timePacket.SerializeToString()
signed_pb = signing.sign(pb_string, AES_KEY)

MFW_VERSION = "3299"
TFW_VERSION = "321"
headers = {
  'Content-type': 'application/x-protobuf',
  'X-Hello-Sense-Id': DEVICE_ID,
  'X-Hello-Sense-MFW': MFW_VERSION,
  'X-Hello-Sense-TFW': TFW_VERSION,
  'X-Forwarded-For': '123.123.123.124'
}

#sys.exit(1)
while True:
  resp = requests.post(ENDPOINT + 'time/', headers=headers, data=signed_pb)
  print "**** RESPONSE ****"
  print resp.raw	
  print resp.headers
  print resp.status_code
  print resp.encoding
  
  if resp.status_code != 200:
    sys.exit(resp.content)
  print "Body length", len(resp.content)
  print "**** END RESPONSE ****"

  server_pb_string = signing.verify_signature(resp.content, AES_KEY)
  timeResp = ntp_pb2.NTPDataPacket()
  timeResp.ParseFromString(server_pb_string)

  print '-' * 10
  print timeResp
  print '-' * 10
  time.sleep(1)
  break
