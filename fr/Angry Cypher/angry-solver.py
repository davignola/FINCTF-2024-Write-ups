def encrypt_decrypt(data: str, key: int) -> str:
    # Convert key to bytes
    key_bytes = [
        key & 0xFF,
        (key >> 8) & 0xFF,
        (key >> 16) & 0xFF,
        (key >> 24) & 0xFF
    ]
    
    pos = 0
    result = []
    
    # XOR each byte of the data with the key bytes
    while pos < len(data):
        keyCycle = pos % 4
                
        encrypted_char = chr(data[pos] ^ key_bytes[keyCycle])
        result.append(encrypted_char)
        
        pos += 1
    
    return ''.join(result)

def recover_key(encrypted_data: str, prefix: str) -> int:
    # Grab the corresponding prefix from the encrypted data
    encrypted_prefix = encrypted_data[:len(prefix)]
    
    # Recover the 4 key bytes, if the lenght is more than 4, just roll over
    key_bytes = [0] * 4
    for i in range(len(prefix)):
        key_bytes[(i) % 4] = encrypted_prefix[i] ^ ord(prefix[i])
    
    # Reconstruct the int32 key from the bytes
    key = (key_bytes[3] << 24) | (key_bytes[2] << 16) | (key_bytes[1] << 8) | key_bytes[0]
    
    return key

encrypted_data = "lq/Ss4Sg57+ygOmDs4fomb+IvJm+xv6ZvofumbWVvIK1h/Ccqcb4n/CB+YTwk/KZs4nunqPG/Z63lOWN" 
decoded_data = b'\x96\xaf\xd2\xb3\x84\xa0\xe7\xbf\xb2\x80\xe9\x83\xb3\x87\xe8\x99\xbf\x88\xbc\x99\xbe\xc6\xfe\x99\xbe\x87\xee\x99\xb5\x95\xbc\x82\xb5\x87\xf0\x9c\xa9\xc6\xf8\x9f\xf0\x81\xf9\x84\xf0\x93\xf2\x99\xb3\x89\xee\x9e\xa3\xc6\xfd\x9e\xb7\x94\xe5\x8d'
print("Encrypted:", decoded_data)

# Key recovery
prefix = "FINCTF{"
recovered_key = recover_key(decoded_data, prefix)
print("Recovered Key:", hex(recovered_key))

# Use the recovered key on the encrypted data
decrypted_data = encrypt_decrypt(decoded_data, recovered_key)
print("Decrypted:", decrypted_data)

