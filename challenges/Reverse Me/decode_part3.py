import itertools

expected = bytearray(b"nndrdylrsmvzswybaxlul")
off_804C17C = bytearray(b'\x37\x35\x36\x38\x35\x31\x36\x35\x34\x32\x32\x39\x33\x33\x39\x34\x37\x35\x32\x38\x38\x34\x39\x34\x31\x31\x37\x35\x39\x33\x36\x37\x32\x31\x38\x31\x34\x39\x38\x33\x33\x36\x32\x37\x36\x00')
off_804C170 = bytearray(b'\x32\x32\x36\x34\x39\x33\x37\x34\x38\x38\x35\x36\x35\x36\x37\x33\x32\x39\x33\x37\x33\x36\x37\x38\x37\x31\x31\x35\x37\x35\x39\x39\x34\x31\x34\x32\x33\x32\x32\x36\x39\x36\x38\x34\x35')
off_804C174 = bytearray(b'\x38\x32\x37\x33\x39\x39\x32\x36\x35\x38\x35\x37\x31\x35\x34\x36\x32\x33\x31\x38\x33\x39\x35\x32\x37\x36\x38\x39\x34\x34\x34\x36\x36\x33\x35\x39\x32\x31\x31\x37\x37\x33\x31\x34\x38')
off_804C178 = bytearray(b'\x39\x37\x39\x31\x33\x39\x31\x35\x34\x36\x36\x33\x38\x37\x32\x39\x35\x37\x34\x31\x34\x37\x37\x38\x33\x36\x32\x35\x34\x38\x39\x31\x33\x38\x34\x39\x34\x35\x33\x33\x35\x32\x36\x37\x38')


# The byte encoding function
def FUN_080493e7(a1, a2, a3):
    if a1 <= 96 or a1 > 122:
        print("Try again.")
        exit(1)
    return ((a2 * a3 + a1 - 97) % 256 + 97 + (a2 << 8)) % 26 + 97


# The crypting loop
def encode(password):
    for i in range(len(password)):
        password[i] = FUN_080493e7(
            password[i],
            off_804C17C[off_804C17C[i] % 40],
            (off_804C170[i] + off_804C174[2 * i] + off_804C178[2 * i]) % 256
        )
    return password


# Iterate through all possible [a-z] passwords until the expected output is found
def brute_force(expected):
    charset = ''.join(chr(i) for i in range(97, 123))  # Characters from 'a' to 'z'
    max_length = len(expected) 
    password = bytearray() 

    for i in range(max_length):
        for char in charset:
            tmp_pwd = password + bytearray(char.encode())
            encoded = encode(tmp_pwd.copy())
            if encoded[i] == expected[i]:
                password = tmp_pwd
                break

    print(f"Password found: {tmp_pwd.decode('utf-8')}")
    return



if __name__ == "__main__":
    brute_force(expected)
