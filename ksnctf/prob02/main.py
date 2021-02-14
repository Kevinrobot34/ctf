N_ALPH = 26
TARGET = '''
EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu
gur yrggre KVVV yrggref nsgre vg va gur nycunorg.
EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr.
Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.
'''


def caesar(s: str, r: int) -> str:
    t_list = []
    for si in s:
        if ord('a') <= ord(si) <= ord('z'):
            t_list.append(chr(ord('a') + (ord(si) - ord('a') + r) % N_ALPH))
        elif ord('A') <= ord(si) <= ord('Z'):
            t_list.append(chr(ord('A') + (ord(si) - ord('A') + r) % N_ALPH))
        else:
            t_list.append(si)
    return ''.join(t_list)


for i in range(1, 26):
    print(i)
    print(caesar(TARGET, i))
