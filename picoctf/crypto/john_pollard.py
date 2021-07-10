import sympy
from Crypto.PublicKey import RSA
from Crypto.Util.number import isPrime

fn = 'cert'
with open(fn, 'r') as reader:
    key = RSA.import_key(reader.read())
print(key.__dict__)

factors: dict = sympy.factorint(key.n)  # type: ignore
print(factors)
assert len(factors) == 2
assert all(ci == 1 for ci in factors.values())
assert all(isPrime(fi) for fi in factors.keys())
p, q = factors.keys()
assert key.n == p * q

flag1 = f'picoCTF{{{p},{q}}}'
flag2 = f'picoCTF{{{q},{p}}}'
print(flag1)
print(flag2)
