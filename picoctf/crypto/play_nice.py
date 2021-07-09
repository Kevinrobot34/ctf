from telnetlib import Telnet

SQUARE_SIZE = 6
HOST = 'mercury.picoctf.net'
PORT = 40742


def generate_square(alphabet):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    matrix = []
    row = []
    for i, letter in enumerate(alphabet):
        if i % SQUARE_SIZE == 0:
            row = []
        row.append(letter)
        if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
            matrix.append(row)
    return matrix


def get_index(letter, matrix):
    for row in range(SQUARE_SIZE):
        for col in range(SQUARE_SIZE):
            if matrix[row][col] == letter:
                return (row, col)
    print("letter not found in matrix.")
    exit()


def decrypto_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:
        return matrix[p1[0]][(p1[1] - 1) % SQUARE_SIZE] + matrix[p2[0]][
            (p2[1] - 1) % SQUARE_SIZE]
    elif p1[1] == p2[1]:
        return matrix[(p1[0] - 1) % SQUARE_SIZE][p1[1]] + matrix[
            (p2[0] - 1) % SQUARE_SIZE][p2[1]]
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


def decrypt_string(crypt, matrix):
    result = ""
    for i in range(0, len(crypt), 2):
        result += decrypto_pair(crypt[i:i + 2], matrix)
    return result


with Telnet(HOST, PORT) as tn:
    ret = tn.read_until(b'What is the plaintext message?')
    alphabet = str(ret).split('Here is the alphabet: ')[1].split(r'\n')[0]
    m = generate_square(alphabet)
    enc_msg = str(ret).split('Here is the encrypted message: ')[1].split(
        r'\n')[0]
    print(alphabet)
    print(enc_msg)

    msg = decrypt_string(enc_msg, m)
    tn.write(msg.encode('ascii') + b'\n')
    ret2 = tn.read_all()
    print(ret2)
