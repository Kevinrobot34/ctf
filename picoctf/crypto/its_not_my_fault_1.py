import hashlib
import math
import random
from telnetlib import Telnet
from typing import Optional

HOST = 'mercury.picoctf.net'
PORT = 41175


def md5_pow(str_start: str,
            hash_end: str,
            n_max_trial: int = 100_000_000) -> Optional[str]:
    for i in range(1, n_max_trial):
        if i % 10_000_000 == 0:
            print("i:" + str(i))
        s = f'{str_start}{i}'
        md5 = hashlib.md5(s.encode()).hexdigest()
        if md5[-6:] == hash_end:
            return s
    return None


def solution(n: int, e: int, n_trial: int = 5) -> Optional[int]:
    for trial in range(n_trial):
        print(f'Trial #{trial}')
        x = random.randint(2, n // 2)
        x_pow = x_pow_base = pow(x, e, n)
        for _ in range(1, 1 << 20):
            y = (x_pow - x) % n
            p = math.gcd(y, n)
            if p != 1 and n % p == 0:
                q = n // p
                print('p:', p)
                print('q:', q)
                return p + q
            x_pow *= x_pow_base
            x_pow %= n
    return None


with Telnet(HOST, PORT) as tn:
    # PoW phase
    print('Start: md5 PoW')
    ret0 = tn.read_until(b'\n').decode()
    str_start = ret0.split('"')[1]
    hash_end = ret0.split(': ')[1].rstrip()
    pow_res = md5_pow(str_start, hash_end)
    if not pow_res:
        print('Fail: md5 PoW')
        exit(1)

    tn.write(pow_res.encode() + b'\n')
    print('Finish: md5 PoW')

    # main phase
    print('Start: main part')
    ret1 = tn.read_until(b'\n').decode()
    n = int(ret1.split(':  ')[1])
    ret2 = tn.read_until(b'\n').decode()
    e = int(ret2.split(':  ')[1])
    print('n:', n)
    print('e:', e)

    p_plus_q = solution(n, e)
    if not p_plus_q:
        print('Fail: main part')
        exit()

    tn.write(str(p_plus_q).encode() + b'\n')
    ret3 = tn.read_until(b'\n').decode()
    print(ret3)
    print('Finish: main part')
