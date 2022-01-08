import random
import signal

from Crypto.Util.number import bytes_to_long, getPrime

message = b""
for _ in range(128):
    message += b"o" if random.getrandbits(1) == 1 else b"O"

M = getPrime(len(message) * 5)
S = bytes_to_long(message) % M
print('generated message', message)
print(f'M={M}')
print(f'S={S}')

message_true = None
for t in range(100):
    # t = 0
    n = 128
    c = sum(79 * pow(256, i, M) for i in range(n)) % M
    c = int(c)

    mat_list = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        mat_list[i][n] = 32 * pow(256, i, M) % M
    tm = t * M

    mat_list[n][n] = c - S - tm
    for i in range(n):
        mat_list[i][i] = 1
    mat_list
    mat = matrix(ZZ, mat_list).LLL()
    # print(t, mat[0])

    print(f't={t}')
    for row in mat:
        if row[-1] != 0:
            continue
        if all(row_i in [0, 1] for row_i in row[:n]):
            print(t, row)
            message_true = ''.join('Oo'[row[i]] for i in range(n))[::-1]
            break
    if message_true is not None:
        print('Found true message!')
        print(message_true)
        print('Check', message.decode() == message_true)
        break
