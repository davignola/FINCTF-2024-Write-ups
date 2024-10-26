crypted = b'\x0f\x2f\x86\x7a\x3e\x23\x23\x4e\x14\x30\x62\x15\x1b\x26\x12\x41\x47\x1e\x2c\x64\x46\x32\x3f\x22\x16\x26\x47'
key =     b'\x4e\x61\x31\x30\x63\x5a\x31\x34\x78\x4a\x33\x51\x77\x6d\x72\x4a\x34\x78\x7a\x30\x4a\x48\x50\x44\x78\x70\x37'
lenght = len(crypted) # 0x1b == 27

# Buffer for the result
buffer = bytearray(lenght)

for i in range(lenght):
    # Encrypt function adds 7 to the input, so we need to subtract for decryption
    buffer[i] = (crypted[i] - 7) ^ key[i]

# Convert the buffer to a string
result = ''.join(chr(b) for b in buffer)

print(result)