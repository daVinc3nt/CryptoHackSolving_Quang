enc_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
c = bytes.fromhex(enc_hex)
print(c)
# known plaintext
known = b"crypto{"
key_part = bytes([c[i] ^ known[i] for i in range(len(known))])
last_key_byte = c[-1] ^ ord('}')
key = key_part + bytes([last_key_byte])   # b"myXORkey"

pt = bytes(c[i] ^ key[i % len(key)] for i in range(len(c)))
print(pt.decode())
