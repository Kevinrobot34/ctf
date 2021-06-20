import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain: str) -> str:
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(enc: str) -> str:
    plain = ""
    for i in range(0, len(enc), 2):
        b0 = ord(enc[i]) - LOWERCASE_OFFSET
        b1 = ord(enc[i + 1]) - LOWERCASE_OFFSET

        plain += chr(b0 * 16 + b1)
    return plain


def shift(c: str, k: str) -> str:
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = "redacted"
key = "a"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
print(enc)

# target
enc = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
for k in ALPHABET:
    enc_shifted = ''.join(map(lambda x: shift(x, k), enc))
    print('-' * 80)
    print(k, b16_decode(enc_shifted))
