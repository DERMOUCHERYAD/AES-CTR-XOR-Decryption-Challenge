#!/usr/bin/env python3
from Crypto.Hash import MD5
from datetime import datetime
import binascii

# Message test connu (le plaintext utilisé dans le chiffrement)
test_plaintext = b"Capybara friends, mission accomplished! We've caused a blackout, let's meet at the bar to celebrate!"

# Contenu du fichier output.txt fourni (2 lignes : 1ère ligne pour le message test, 2ème pour le flag)
lines = [
    "2025-03-10 09:50:07.974000 ac0720038488a5f6f149cf0f3a41e31ffff996363fa6a0cf493c2a2998ad0bddfab0422efd4df201bf05ede07926ce3988015bb35a717504d03db4a0ac52d67c8f006b9e662f0db0a6644484d210eb33d3ce54d9565c10bb2fcc08d8db5e87d96d576418",
    "2025-03-10 09:50:10.975000 b571b8eb470f7c3b466618af91cb111184d73bfca56c3f1ddc44c5845f789f8584d7a6fe60d3328b386a0044b8e1164bb810f97398e8b98d280903220dc33452be73e90fefa9"
]

# Fonction pour extraire la date et le ciphertext hex de chaque ligne
def parse_line(line):
    parts = line.split()
    # La date se compose des deux premiers éléments
    date_str = " ".join(parts[0:2])
    # Le ciphertext correspond au reste (sans espaces)
    ct_hex = "".join(parts[2:])
    return date_str, ct_hex

date_test_str, ct_test_hex = parse_line(lines[0])
date_flag_str, ct_flag_hex = parse_line(lines[1])

# Fonction pour calculer la valeur "ts" à partir de la date
def get_ts(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    ts_float = round(dt.timestamp(), 3)
    ts_int = int(ts_float * 1000)
    ts_bytes = ts_int.to_bytes(16, byteorder='big')
    h = MD5.new()
    h.update(ts_bytes)
    return h.digest()

ts_test = get_ts(date_test_str)
ts_flag = get_ts(date_flag_str)

# Fonction pour faire le XOR d'une donnée par blocs de la taille de 'block'
def xor_blocks(data, block):
    out = b""
    for i in range(0, len(data), len(block)):
        chunk = data[i:i+len(block)]
        block_part = block[:len(chunk)]
        out += bytes(a ^ b for a, b in zip(chunk, block_part))
    return out

# Convertir les ciphertext hex en bytes
ct_test_masked = binascii.unhexlify(ct_test_hex.strip())
ct_flag_masked = binascii.unhexlify(ct_flag_hex.strip())

# Annuler le XOR avec "ts" pour obtenir le véritable ciphertext AES-CTR
ct_test_aes = xor_blocks(ct_test_masked, ts_test)
ct_flag_aes = xor_blocks(ct_flag_masked, ts_flag)

# Récupérer le keystream à partir du message test connu
if len(test_plaintext) != len(ct_test_aes):
    print("La taille du message test ne correspond pas !")
else:
    keystream = bytes(a ^ b for a, b in zip(test_plaintext, ct_test_aes))
    # Décrypter le flag en faisant XOR entre le ciphertext AES du flag et le keystream
    flag_plaintext = bytes(a ^ b for a, b in zip(ct_flag_aes, keystream))
    print("Flag décrypté :", flag_plaintext.decode(errors='replace'))
