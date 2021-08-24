from telnetlib import Telnet

HOST = 'jupiter.challenges.picoctf.org'
PORT = 15130


def convert(target: list[str], base: int) -> str:
    ret = []
    for ti in target:
        ret.append(chr(int(ti, base)))
    return ''.join(ret)


with Telnet(HOST, PORT) as tn:
    # first problem
    _ = tn.read_until(b'\n').decode()
    _ = tn.read_until(b'\n').decode()
    ret1 = tn.read_until(b'\n').decode()
    ret1 = ret1.removeprefix('Please give the ')
    ret1 = ret1.removesuffix(' as a word.\n')
    target_chr1 = ret1.split()
    _ = tn.read_until(b'\n').decode()
    _ = tn.read_until(b'\n').decode()
    _ = tn.read_until(b'\n').decode()
    _ = tn.read_until(b'\n').decode()
    ans1 = convert(target_chr1, 2)
    tn.write(ans1.encode() + b'\n')
    print('ans1', ans1)

    # second problem
    ret2 = tn.read_until(b'\n').decode()
    ret2 = ret2.removeprefix('Please give me the ')
    ret2 = ret2.removesuffix(' as a word.\n')
    target_chr2 = ret2.split()
    _ = tn.read_until(b'\n').decode()
    print(ret2)
    ans2 = convert(target_chr2, 8)
    tn.write(ans2.encode() + b'\n')
    print('ans2', ans2)

    # third problem
    ret3 = tn.read_until(b'\n').decode()
    ret3 = ret3.removeprefix('Please give me the ')
    ret3 = ret3.removesuffix(' as a word.\n')
    target_chr3 = [ret3[i:i + 2] for i in range(0, len(ret3), 2)]
    _ = tn.read_until(b'\n').decode()
    print(ret3)
    ans3 = convert(target_chr3, 16)
    print('ans3', ans3)
    tn.write(ans3.encode() + b'\n')

    # Finish! Get flag!
    print(tn.read_until(b'\n').decode())
    print(tn.read_until(b'\n').decode())
