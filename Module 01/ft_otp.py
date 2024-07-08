#!/usr/bin/env python3

import sys
import os
import time
import hmac
import hashlib
import struct
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_key(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_key(key, encrypted_data):
    try:
        f = Fernet(key)
        return f.decrypt(encrypted_data).decode()
    except:
        print("./ft_otp: error: invalid key.")
        sys.exit(1)

def store_key(key_file):
    try:
        with open(key_file, 'r') as f:
            hex_key = f.read().strip()
    except FileNotFoundError:
        print(f"./ft_otp: error: {key_file} not found.")
        sys.exit(1)

    if len(hex_key) != 64 or not all(c in '0123456789abcdefABCDEF' for c in hex_key):
        print("./ft_otp: error: key must be 64 hexadecimal characters.")
        sys.exit(1)
    
    encryption_key = generate_key()
    encrypted_key = encrypt_key(encryption_key, hex_key)

    with open('ft_otp.key', 'wb') as f:
        f.write(encryption_key + b'\n' + encrypted_key)

    print("Key was successfully saved in ft_otp.key.")

def hotp(secret, counter):
    key = bytes.fromhex(secret)
    counter_bytes = struct.pack('>Q', counter)
    hmac_obj = hmac.new(key, counter_bytes, hashlib.sha1)
    hmac_digest = hmac_obj.digest()
    
    offset = hmac_digest[-1] & 0xf
    code = struct.unpack('>I', hmac_digest[offset:offset+4])[0] & 0x7fffffff
    return str(code)[-6:].zfill(6)

def generate_otp(key_file):
    if not os.path.exists(key_file):
        print(f"./ft_otp: error: {key_file} not found.")
        sys.exit(1)

    with open(key_file, 'rb') as f:
        encryption_key = f.readline().strip()
        encrypted_key = f.read()

    hex_key = decrypt_key(encryption_key, encrypted_key)
    
    counter = int(time.time()) // 30
    otp = hotp(hex_key, counter)
    
    print(otp)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./ft_otp -g <key_file> OR ./ft_otp -k <ft_otp.key>")
        sys.exit(1)

    if sys.argv[1] == '-g':
        store_key(sys.argv[2])
    elif sys.argv[1] == '-k':
        generate_otp(sys.argv[2])
    else:
        print("Invalid option. Use -g to store a key or -k to generate an OTP.")
        sys.exit(1)

if __name__ == "__main__":
    main()