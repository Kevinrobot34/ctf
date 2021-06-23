def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt


ctxt = bytes.fromhex(
    '57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637'
)
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it',
]

flag_prefix = b'picoCTF{'
key = b'Africa!'  # set some key
for bit in range(1 << len(random_strs)):
    ctxt1 = ctxt
    for i, rs in enumerate(random_strs):
        if (bit >> i) & 1:
            ctxt1 = encrypt(ctxt1, rs)

    key_cand = encrypt(ctxt1, flag_prefix)[:len(flag_prefix)]
    ptxt_cand = encrypt(ctxt1, key)
    print('-' * 80)
    print(len(ctxt1), ctxt1)
    print('Candidate KEY       :', key_cand)
    print('Candidate Plain text:', ptxt_cand)
