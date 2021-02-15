from collections import Counter

s = '''
oomktvziqtaovmmpxzoqrzsxlpwpgoj
uDQEMISYnnVYnvyWRhHsDXnSCXAVVZj
tZbknedErdpvAwQWpUiLqOxIqpafvXp
dXoAVWcKppbEPuaqmXWjXJwRoRFOoEg
pDiRUXlQjKJlslskVpGwtljGyVJPxHv
bQsQNKxCsdYMdQPJiBmyrsuOrJQOtXg
pMekeinUaMoDXqFzweLKipkBuggnsUv
eQFYCJSKfBgHaJgZnZoWmOmAOJLVQHi
hljrplajyKNXtwmfOjRwOqcqeeplyzy
gkFOltsOyrPgIaerIaSjQQaVMyEhfyd
vEaRHbBzfrcwJbCZmHdddLpuEJwspbt
sXQGkwpKaTZmWJiZzpbkpHNiToawxKn
wJpIKbGhnLjVAJNcxrqkKEJCKCOocSv
mTRDNDpFtRUmcHoRELeSqXoGUIIsuYu
ajeHaSVlQGLaEprSQarDzTomJdAWfqb
zIJLHRBXMvNDegYeaoVRDuWBbdSBtLv
xIeKdAYwajGHMgRLDGgDinBiLNBgatb
kHepNsCQSJjTRmQrCHYWJqIPOVAUOer
rvhmZfmogPglGNuLyAuSivBctlvVfzb
qBJdHUkSaTArlgkhtHPyGhXOPkwmkBq
rvbzZfwvLtTnhyXVHPlwsuGZQnNiNcm
yCMtAVwYVgtZHVNznolGMBETIHFmoWj
wfezbysbvOzsAhxSZFFAfOouyHldEYh
gNHKKSFUtcUxfRyXHMugYBtAxBwDJZh
rHmsozuNeoJqyzMDHsNbUDwzaNLtdxr
bVmQMHyNndOWCZLnhrPxZXCYLDTWQre
aSiEEJjZtoRpUzgsxsiiGzvnRpKLMrk
qTzGCKvNhUhjrmCjAdwQAvkgqHyJZLm
sSxzwjxAnWesTszIxirRwcWIXUPtwwa
nTDEMTRGyhzdCtkTTDWbxdSjsNYlfXz
eawtidzosgaofjxxyfcdoiulemirqap
'''.split('\n')[1:-1]

print(s)
print(len(s), len(s[0]))
N = 31
N_ALPH = 26


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


def reflect(s):
    return [si[::-1] for si in s]


def rot(s):
    return [''.join(s[N - 1 - j][i] for j in range(N)) for i in range(N)]


print(*reflect(s), sep='\n')
print()
print(*rot(s), sep='\n')
print()
print(*rot(rot(s)), sep='\n')
print(Counter(list(''.join(s))))
print()

for i in range(N_ALPH):
    print(i, caesar('GRTMEDT', i))

r = 13
print(*[caesar(si, r) for si in s], sep='\n')
print()
print(*[''.join('_' if 'a' <= sij <= 'z' else '#' for sij in si) for si in s],
      sep='\n')
print()
