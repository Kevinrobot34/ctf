# picoCTF / crypto
## Classic Cipher
### Mod 26
* Solution
  * ROT13やるだけ
  * 自分で組んでも良いし、コマンド叩いても良い
* Flag
  * `picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}`
  * "Next time I'll try to rounds of rot13"
  * 最後のランダム文字列的なやつは、定期的に出題側が書き換えているっぽいやつ


### 13
* Solution
  * ROT13やるだけ
  * "Mod 26" と被っているのに何故...
* Flag
  * `picoCTF{not_too_bad_of_a_problem}`


### caesar
* Solution
  * シーザー暗号だと思われるので、keyを0-25まで全て試して、それっぽい文字列を探す
* Flag
  * `picoCTF{crossingtherubiconvfhsjkou}`
  * "crossing the rubicon"
    * ユリウス・カエサルはルビコン川を渡って後戻りのできない戦へと踏み出したらしい


### New Caesar
* Solution
  * `new_caesar.py` を見る
    * `b16_encode` でアルファベットを適当に前半16文字に変換
    * `shift` はアルファベット前半16文字に絞ったシーザー暗号的な感じ
  * 簡単なのでdecodeのコードを書いて、keyを26種類総当たりする
  * "redacted" は「編集済み」という意味
* Flag
  * `picoCTF{et_tu?_23217b54456fb10e908b5e87c6e89156}`
  * "et tu ?"
    * "Et tu, Brute?" で「ブルータス、お前もか」という意味のラテン語
  * 最後の `_` 以降は定期的に出題側が書き換えているっぽいやつ


### Easy1
* Solution
  * いわゆるヴィジュネル暗号
    * ヴィジュネル暗号は端的に言うとブロック化したシフト暗号
    * 問題で与えられているような表のcolumnが平文の文字、indexが鍵の文字、valueが暗号文の文字と対応している
    * 具体的な手順は以下
      * 鍵が平文と同じ長さになるように反復させる/削る
      * 平文と鍵のi文字目を見て、表を元に暗号文のi文字目を決定するだけ
  * 文字ごとにシーザー暗号的なことすれば良いだけ
* Flag
  * `picoCTF{CRYPTOISFUN}`


### spelling-quiz
* Solution
  * いわゆる単一換字式暗号
    * 頻度分析による解読方法が知られている
  * 自分でやるのは辛いので、適当なsolverを使うと楽
    * https://www.quipqiup.com/
    * https://www.guballa.de/substitution-solver
* Flag
  * `picoCTF{perhaps_the_dog_jumped_over_was_just_tired}`


## Common Key Crypto
### XtraORdinary
* Solution
  * `encrypt.py` を見る
    * まず `flag` と `key` をbyteごとにxorとって `ctxt` とする
    * `ctxt` と `random_strs` の各要素をランダムにたくさんXORしてそれを最終的な `ctxt1` とする
  * これを踏まえまず、 `random_strs` の各要素を高々１度XOR取ったもの32種類が、 `encrypt(flag, key)` の候補
  * `picoCTF{` から始まるはずなので、上記32種類全てと `picoCTF{` のXORを取ってみると、 `key` の候補が得られる
  * 上記 `key` を `ctxt1` とXOR取って `flag` が出てくる
* Flag
  * `picoCTF{w41t_s0_1_d1dnt_1nv3nt_x0r???}`
  * "wait so I didn't invent xor?"


## RSA
### Mind your Ps and Qs
* Solution
  * Modulus `n` が小さいため、素因数分解が可能になってしまう
    * やり方はいくつかある
      * http://factordb.com/
        * [未確認] https://pypi.org/project/factordb-pycli/
      * [未確認] https://pypi.org/project/primefac/
      * [未確認] https://github.com/Ganapati/RsaCtfTool
  * `n = p * q` と表せたら、あとは秘密鍵を拡張ユークリッドの互除法で計算するだけ
* Flag
  * `picoCTF{sma11_N_n0_g0od_55304594}`
  * "small N no good"


### miniRSA
* Solution
  * "Low Public Exponent Attack" をやれば良い
  * 変数
    * `m` : Plain Text
    * `c` : Cipher Text
    * `e` : Public Exponent
    * `n` : Modulus
  * `m**e < n` であれば直接二分探索で `m` を探すだけ
    * 実際に見つかる
* Flag
  * `picoCTF{n33d_a_lArg3r_e_606ce004}`
  * "need a large e"


### Mini RSA
* Solution
  * いわゆる "Low Public Exponent Attack" をやれば良い
  * 変数
    * `m` : Plain Text
    * `c` : Cipher Text
    * `e` : Public Exponent
    * `n` : Modulus
  * `m**e < n` であれば直接二分探索で `m` を探すだけだが、今回は「ギリギリ」これが成立しないように平文をpaddingしたと言っている
  * `c` に順次 `n` を足していきながら、 `e`乗根を整数で求められるか試してみれば良い
  * pythonで適当に書いても数分で見つかる
* Flag
  * `picoCTF{e_sh0u1d_b3_lArg3r_7adb35b1}`
  * "e should be larger"


### Triple Secure
* Solution
  * 違う公開鍵のRSAで３回暗号化している
  * ただ、 `n1 = p * q` / `n2 = p * r` / `n3 = q * r` としてしまっているので簡単に各素数が求まっちゃう
    * やり方１
      * `math.isqrt(n1 * n2 * n3)` 
      * https://docs.python.org/ja/3/library/math.html#math.isqrt
    * やり方２
      * `p = math.gcd(n1, n2)`
      * gcdは `O(log min(n1, n2)` なので十分高速
* Flag
  * `picoCTF{1_gu3ss_tr1pl3_rs4_1snt_tr1pl3_s3cur3!!!!!!}`
  * "I guess triple rsa isn't triple secure!"


### college-rowing-team
* Solution
  * いわゆる "Håstad's broadcast attack" の問題
    * 状況としてはpublic exponent `e`を小さい数（今回は３）で固定して、ある平文 `m` を `e` 個の公開鍵で暗号化した暗号文が与えられている
    * 与えられるmodulusを`n1/n2/n3`、対応する暗号文を`c1/c2/c3`とする
      * `m^e ≡ c1 mod n1`
      * `m^e ≡ c2 mod n2`
      * `m^e ≡ c3 mod n3`
    * よって中国剰余定理を使うことで `m^e mod (n1*n2*n3)` が求まる
    * ここで、平文`m`は `m < ni` を満たす（そうでないと平文がtruncateされてしまうので）
    * つまり `m^e = m^3 < n1 * n2 * n3` であり上記CRTで求めた値は `m^e` そのもの
    * よってあとは`e`乗根を二分探索やライブラリで求めれば終わり
  * 今回の設定では、flagとその他の適当な文章3つの合計4つの文字列が、それぞれ3回ずつ暗号化されている
  * 各暗号文がどの平文に対応するかは分からないので、brute-forceに全パターン試す
* Flag
  * `picoCTF{1_gu3ss_p30pl3_p4d_m3ss4g3s_f0r_4_r34s0n}'`
  * "I guess people pad messages for a reason"
* References
  * https://partender810.hatenablog.com/entry/2021/05/19/210459#college-rowing-team-250pt
  * https://en.wikipedia.org/wiki/Coppersmith%27s_attack



## Others
### The Numbers
* Solution
  * 画像を見ると明らかにFlagっぽい文字列が数字に変換されて並んでいる
  * CTFに相当しそうな文字列が `3, 20, 6` なので、アルファベットの前から何番目かで変換されてると予想できる。
* Flag
  * `PICOCTF{THENUMBERSMASON}`
  * なぜか全部大文字...


### Pixelated
* Solution
  * 二つの画像を重ねる
  * 重ねる方法はいろいろある(AND/OR/XOR/...)が今回は単純に和をとるだけ
* Flag
  * `picoCTF{d562333d}`
  * 今回のFlagは毎回変わるタイプらしい