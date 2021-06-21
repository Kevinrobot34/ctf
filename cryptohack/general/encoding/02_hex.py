from Crypto.Util.number import long_to_bytes

flag_hex = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# solution 1
flag_ = 0x63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
print(long_to_bytes(flag_))
print(long_to_bytes(int(flag_hex, 16)))
# solution 2
print(bytes.fromhex(flag_hex))
# solution 3
print(''.join(
    map(chr,
        [int(flag_hex[i:i + 2], 16) for i in range(0, len(flag_hex), 2)])))
