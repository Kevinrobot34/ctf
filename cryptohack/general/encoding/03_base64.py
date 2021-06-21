import base64

from Crypto.Util.number import long_to_bytes

flag_hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
flag_bytes = long_to_bytes(int(flag_hex, 16))
flag = base64.b64encode(flag_bytes)
print(flag)
