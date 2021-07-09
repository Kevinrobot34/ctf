from fractions import Fraction
from math import ceil
from telnetlib import Telnet

from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes

HOST = 'mercury.picoctf.net'
PORT = 10333
TARGET_SENTENCE = 'Give me ciphertext to decrypt: '


class Oracle:
    def __init__(self, host: str, port: int, target_sentence: str):
        self.host = host
        self.port = port
        self.target_sentence = target_sentence
        self.tn = Telnet(host, port)
        ret = self.read()
        self.n = int(ret.split('n: ')[1].split(r'\n')[0])
        self.e = int(ret.split('e: ')[1].split(r'\n')[0])
        self.c = int(ret.split('ciphertext: ')[1].split(r'\n')[0])

    def __del__(self):
        self.tn.close()

    def read(self, encode: str = 'utf-8') -> str:
        return str(self.tn.read_until(self.target_sentence.encode(encode)))

    def send(self, target_c: int) -> int:
        '''
        get result of decryption
        '''
        self.tn.write(str(target_c).encode('ascii') + b'\n')
        ret = self.read()
        m = int(ret.split('Here you go: ')[1].split(r'\n')[0])
        return m

    def send2(self, target_c: int) -> bool:
        return self.send(target_c) % 2 == 1


def solution1():
    oracle = Oracle(HOST, PORT, TARGET_SENTENCE)
    m = oracle.send(oracle.c + oracle.n)
    print(long_to_bytes(m))


def solution2():
    oracle = Oracle(HOST, PORT, TARGET_SENTENCE)
    m_ = oracle.send(oracle.c * pow(2, oracle.e, oracle.n) % oracle.n)
    m = m_ * inverse(2, oracle.n) % oracle.n
    print(long_to_bytes(m))


def solution3():
    '''
    LSB Decryption Oracle Attack
    '''
    oracle = Oracle(HOST, PORT, TARGET_SENTENCE)
    lb = Fraction(0)
    ub = Fraction(oracle.n)
    cnt = 1
    while ub - lb > 1 and cnt < 10000:
        mid = Fraction(lb + ub, 2)
        if cnt < 600:
            oracle_res = False
        else:
            c_ = oracle.c * pow(2, oracle.e * cnt, oracle.n) % oracle.n
            oracle_res = oracle.send2(c_)
        if oracle_res:
            lb = mid
        else:
            ub = mid
        cnt += 1
        print(cnt, oracle_res)
    m = ceil(lb)
    print(long_to_bytes(m))


solution1()
solution2()
solution3()
