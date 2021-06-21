c = 'picoCTF{ynkooejcpdanqxeykjrbdofgkq}'
c0 = 'ynkooejcpdanqxeykjrbdofgkq'  # cspell: disable-line


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


for i in range(26):
    print(i, rot(c0, i))
