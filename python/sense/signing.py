import hashlib
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