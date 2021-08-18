def encrypt(flag: str) -> str:
    return ''.join([
        chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
        for i in range(0, len(flag), 2)
    ])


def decrypt(flag_enc: str) -> str:
    return ''.join([
        chr(ord(flag_enc[i]) >> 8) + chr(ord(flag_enc[i]) % (1 << 8))
        for i in range(len(flag_enc))
    ])


assert decrypt(encrypt('abcd')) == 'abcd'

flag_enc = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'
flag = decrypt(flag_enc)
print(flag)
