#!/usr/bin/env python3
from pwn import remote
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode_challenge(ch_type, encoded):
    if ch_type == "base64":
        return base64.b64decode(encoded).decode()
    elif ch_type == "hex":
        return bytes.fromhex(encoded).decode()
    elif ch_type == "rot13":
        return codecs.decode(encoded, "rot_13")
    elif ch_type == "bigint":
        return long_to_bytes(int(encoded, 16)).decode()
    elif ch_type == "utf-8":
        return "".join(chr(x) for x in encoded)
    else:
        raise ValueError("Unknown type: " + ch_type)

while True:
    received = json_recv()

    if "flag" in received:
        print("FLAG:", received["flag"])
        break

    print("Received type:", received["type"])
    print("Received encoded value:", received["encoded"])

    decoded = decode_challenge(received["type"], received["encoded"])

    to_send = {"decoded": decoded}
    json_send(to_send)
