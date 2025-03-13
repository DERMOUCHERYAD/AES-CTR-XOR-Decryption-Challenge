from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import time
from datetime import datetime
import random
import hashlib

KEY = os.urandom(16)

def generate_timestamp():
    timestamp = time.time()
    timestamp_ms = round(timestamp,3)   
    date = datetime.fromtimestamp(timestamp_ms)

    timestamp_int = int(timestamp_ms * 1000)
    ts = timestamp_int.to_bytes(16, byteorder='big') 
    return str(date),hashlib.md5(ts).digest()

def encryption(plaintext):
    date, ts = generate_timestamp()
    c = Counter.new(128)
    cipher = AES.new(KEY, AES.MODE_CTR, counter=c)
    ciphertext = cipher.encrypt(plaintext)
    ciphertext_blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    ciphertext_with_xor = b''

    for block in ciphertext_blocks:
        block_with_xor = bytes(a ^ b for a, b in zip(block, ts))
        ciphertext_with_xor += block_with_xor

    time.sleep(random.randint(3,7))
    return date, ciphertext_with_xor.hex()

test = b"Capybara friends, mission accomplished! We've caused a blackout, let's meet at the bar to celebrate!"

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()

with open('output.txt', 'w') as f:
    f.write(" ".join(encryption(test)) + "\n" + " ".join(encryption(flag)))