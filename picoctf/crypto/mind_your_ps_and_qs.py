from math import gcd

from Crypto.Util.number import long_to_bytes


# return (g, x, y) which satisfies ax + by = g and g = GCD(a,b)
def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b:
        g, y, x = ext_gcd(b, a % b)
        y -= (a // b) * x
        return g, x, y
    return a, 1, 0


c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537

# use factordb: http://factordb.com/
p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809
phi = (p - 1) * (q - 1)
assert n == p * q
assert gcd(e, phi) == 1

# get private key
_, d, _ = ext_gcd(e, phi)

# decrypto
m = pow(c, d, n)
print(long_to_bytes(m))
