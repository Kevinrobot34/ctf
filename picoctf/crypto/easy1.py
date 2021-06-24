def rot(text: str, k: int = 13) -> str:
    l = []
    for ti in text:
        if ord('a') <= ord(ti) <= ord('z'):
            l.append(chr((ord(ti) - ord('a') + k) % 26 + ord('a')))
        elif ord('A') <= ord(ti) <= ord('Z'):
            l.append(chr((ord(ti) - ord('A') + k) % 26 + ord('A')))
        else:
            l.append(ti)
    return ''.join(l)


c = 'UFJKXQZQUNB'  # cspell: disable-line
key = 'SOLVECRYPTO'

m = ''
for i in range(len(c)):
    m += rot(c[i], -ord(key[i]) + ord('A'))
print(m)
