import requests
import json
import sys
import periodic_pb2
import time
import sys
import hashlib
import sync_response_pb2
import signing

ENDPOINT = "http://127.0.0.1:5555/" if len(sys.argv) == 1 else "https://sense-in.hello.is/"
#ENDPOINT = "https://sense-in.hello.is/"

#ENDPOINT = "https://dev-in.hello.is/"

print ENDPOINT

#MY Home Device

DEVICE_ID = "fake-sense"
AES_KEY = "0C95235EDF61C28FDDF5971C148BA9A2"

#DEVICE_ID = "0000000000000000"
#AES_KEY = "31323334353637383931323334353637" #default key

MFW_VERSION = "4036"
TFW_VERSION = "321"

batch = periodic_pb2.batched_periodic_data()
batch.firmware_version= int(MFW_VERSION)
batch.uptime_in_second=12345
batch.device_id=DEVICE_ID
batch.messages_in_queue = 1

for i in range(2):
  periodic_data = batch.data.add()

  periodic_data.temperature = 2466
  periodic_data.light = 100
  periodic_data.light_variability = 0
  periodic_data.light_tonality = 273
  periodic_data.humidity = 100
  periodic_data.dust = 503
  periodic_data.unix_time = int(time.time())

pb_string = batch.SerializeToString()
signed_pb = signing.sign(pb_string, AES_KEY)

headers = {
  'Content-type': 'application/x-protobuf',
  'X-Hello-Sense-Id': DEVICE_ID,
  'X-Hello-Sense-MFW': MFW_VERSION,
  'X-Hello-Sense-TFW': TFW_VERSION,
  'X-Forwarded-For': '123.123.123.124' #199.87.82.114 203.166.220.233
}

#sys.exit(1)
while True:
  resp = requests.post(ENDPOINT + 'in/sense/batch',headers=headers,data=signed_pb)
  print "**** RESPONSE ****"
  print resp.raw	
  print resp.headers
  print resp.status_code
  print resp.encoding
  
  if resp.status_code != 200:
    sys.exit(resp.content)
  print "Body length", len(resp.content)
  print "Body", "".join("{:02x}".format(ord(c)) for c in resp.content)

  print "**** END RESPONSE ****"

  server_pb_string = signing.verify_signature(resp.content, AES_KEY)
  
  sync = sync_response_pb2.SyncResponse()
  sync.ParseFromString(server_pb_string)

  print '-' * 10
  print sync
  print '-' * 10
  print "ringtone_id", sync.alarm.ringtone_id
  print "start_time", sync.alarm.start_time

  print "reset_fw", sync.reset_to_factory_fw
  print "reset_mcu", sync.reset_mcu
  print "Files to download:"
  for f in sync.files:
    print 'Host: ' + f.host
    print 'URL:' + f.url

    r = requests.get('https://'+ f.host + f.url)
    print r.url
    print r.headers
    print r.status_code
    
    m = hashlib.sha1()
    m.update(r.content)
    h = m.hexdigest()
    print "h", h
    
    hh = "".join("{:02x}".format(ord(c)) for c in f.sha1)
    # check sha1 for files
    assert h == hh
  time.sleep(1)
  break
