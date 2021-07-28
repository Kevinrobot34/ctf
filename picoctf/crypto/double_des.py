import binascii
from telnetlib import Telnet

from Crypto.Cipher import DES
from Crypto.Util.number import long_to_bytes

HOST = "mercury.picoctf.net"
PORT = 37751
KEY_SIZE = 10**6


def get_info(input_text: str = '1234') -> tuple[bytes, bytes]:
    target_sentence = b'What data would you like to encrypt? '
    with Telnet(HOST, PORT) as tn:
        # get flag_enc
        ret0 = tn.read_until(target_sentence)
        flag_enc_str = binascii.unhexlify(ret0.split(b'\n')[1].decode())

        # get encrypted text
        tn.write(input_text.encode() + b'\n')
        ret1 = tn.read_until(target_sentence)
        input_enc_str = binascii.unhexlify(ret1.split(b'\n')[0])

        return flag_enc_str, input_enc_str


def pad(msg: str) -> bytes:
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


def search_key(input_bytes: bytes, output_bytes: bytes) -> tuple[bytes, bytes]:
    print('Start seaching keys')
    res_dict = {}
    for i in range(KEY_SIZE):
        key1 = pad(f'{i:06d}')
        cipher1 = DES.new(key1, DES.MODE_ECB)
        ct = cipher1.encrypt(input_bytes)
        res_dict[ct] = key1
    print('Finish first loop')

    for i in range(KEY_SIZE):
        key2 = pad(f'{i:06d}')
        cipher1 = DES.new(key2, DES.MODE_ECB)
        pt = cipher1.decrypt(output_bytes)

        if pt in res_dict:
            print('Get keys!!!!')
            return res_dict[pt], key2

    raise Exception('Failed to search keys')


def main():
    # get info from server
    input_text = '1234'
    input_bytes = pad(binascii.unhexlify(input_text).decode())
    flag_enc_bytes, input_enc_bytes = get_info(input_text)
    print(flag_enc_bytes, input_enc_bytes)

    # search key
    key1, key2 = search_key(input_bytes, input_enc_bytes)
    print(key1, key2)

    # decrypt
    cipher1 = DES.new(key1, DES.MODE_ECB)
    cipher2 = DES.new(key2, DES.MODE_ECB)
    flag = cipher1.decrypt(cipher2.decrypt(flag_enc_bytes)).rstrip().decode()
    print('flag: ', flag)


if __name__ == '__main__':
    '''
    $ nc mercury.picoctf.net 37751
    Here is the flag:
    b49ff20dd1e568c1a62912e207098f2edf56f52d2e703ac633e2f7ffff77724af4d06464e6d5c3ad
    What data would you like to encrypt? 1234
    40615b7f7ff48376
    What data would you like to encrypt?
    '''
    main()
