import requests
import json
import sys
import periodic_pb2
import time
import sys
import hashlib
import sync_response_pb2

from Crypto.Cipher import AES

def sign(pb_string, aeskey):
  """Signs serialized pb with aeskey"""
  m = hashlib.sha1()
  m.update(pb_string)

  print m.digest_size
  print m.hexdigest()

  key = aeskey.decode('hex')

  IV = 16 * '\x00'
  mode = AES.MODE_CBC
  encryptor = AES.new(key, mode, IV=IV)

  b = 12 * '\x00' 

  padded_sha = m.digest() + b
  print len(padded_sha)
  print ":".join("{:02x}".format(ord(c)) for c in padded_sha)
  ciphertext = encryptor.encrypt(padded_sha)
  print "len cipher", len(ciphertext)
  
  print  "".join("{:02x}".format(ord(c)) for c in ciphertext)
  decryptor = AES.new(key, mode, IV=IV)
  plain = decryptor.decrypt(ciphertext)

  assert padded_sha == plain

  return pb_string + IV + ciphertext


def verify_signature(pb_string_with_sig, aeskey):
  server_IV = pb_string_with_sig[:16]
  server_sig = pb_string_with_sig[16:16+32]
  server_body = pb_string_with_sig[16+32:]

  print
  print "server_IV",  "".join("{:02x}".format(ord(c)) for c in server_IV)
  print "server_sig",  "".join("{:02x}".format(ord(c)) for c in server_sig)
  print

  mode = AES.MODE_CBC
  key = aeskey.decode('hex')
  decryptor = AES.new(key, mode, IV=server_IV)
  decrypted = decryptor.decrypt(server_sig)
  decrypted = "".join("{:02x}".format(ord(c)) for c in decrypted)
  print "decrypted sha", decrypted
  # compute sha1 of protobuf body
  m = hashlib.sha1()
  m.update(server_body)

  h = m.hexdigest()

  print "sha", m.hexdigest()
  llen = len(h)
  decrypted_truncated = decrypted[:llen]
  print "decrypted_truncated", decrypted_truncated
  assert h == decrypted_truncated, "hex digest and sig don't match: %s vs %s" % (h, decrypted_truncated)
  return server_body

ENDPOINT = "http://localhost:5555/" if len(sys.argv) == 1 else "https://sense-in.hello.is/"

print ENDPOINT

DEVICE_ID = "fake-sense"
AES_KEY = "0C95235EDF61C28FDDF5971C148BA9A2"

batch = periodic_pb2.batched_periodic_data()
batch.firmware_version=823933775
batch.device_id=DEVICE_ID

for i in range(2):
  periodic_data = batch.data.add()

  periodic_data.temperature = 2685
  periodic_data.light = 152
  periodic_data.light_variability = 1
  periodic_data.light_tonality = 270
  periodic_data.humidity = 3092
  periodic_data.dust = 2857
  periodic_data.unix_time = int(time.time())

pb_string = batch.SerializeToString()

signed_pb = sign(pb_string, AES_KEY)

headers = {
  'Content-type': 'application/x-protobuf',
  'X-Hello-Sense-Id' : DEVICE_ID
}

#sys.exit(1)
while True:
  resp = requests.post(ENDPOINT + 'in/sense/batch',headers=headers,data=signed_pb)
  print resp.raw	
  print resp.headers
  print resp.status_code
  
  if resp.status_code != 200:
    sys.exit(resp.content)
  print "Body length", len(resp.content)
  print "Body", "".join("{:02x}".format(ord(c)) for c in resp.content)

  server_pb_string = verify_signature(resp.content, AES_KEY)
  
  sync = sync_response_pb2.SyncResponse()
  sync.ParseFromString(server_pb_string)

  print '-' * 10
  print "ringtone_id", sync.alarm.ringtone_id
  print "start_time", sync.alarm.start_time
  print "end_time", sync.alarm.end_time
  print "Files to download:"
  for f in sync.files:
    print f.host, f.url, f.serial_flash_filename, f.sha1
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
    #assert h == hh 
  time.sleep(1)
  break
