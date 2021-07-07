from telnetlib import Telnet

from Crypto.Util.number import long_to_bytes

KEY_LEN = 50000
HOST = "mercury.picoctf.net"
PORT = 11188
TARGET_SENTENCE = b'What data would you like to encrypt?'

with Telnet(HOST, PORT) as tn:
    # get flag_enc
    ret0 = tn.read_until(TARGET_SENTENCE)
    flag_enc = str(ret0).split(r'\n')[2]
    flag_len = len(flag_enc) // 2
    flag_enc_bytes = long_to_bytes(int(flag_enc, 16))
    print('flag_enc', len(flag_enc), flag_enc)

    # skip key not related to flag encryption
    tn.write(b'a' * (KEY_LEN - flag_len) + b'\n')
    ret1 = tn.read_until(TARGET_SENTENCE)

    # decrypt flag
    tn.write(flag_enc_bytes + b'\n')
    ret2 = tn.read_until(TARGET_SENTENCE)
    flag_hex = str(ret2).split(r'\n')[1]
    print(long_to_bytes(int(flag_hex, 16)))
