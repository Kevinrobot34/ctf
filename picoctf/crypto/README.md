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


## Others
### The Numbers
* Solution
  * 画像を見ると明らかにFlagっぽい文字列が数字に変換されて並んでいる
  * CTFに相当しそうな文字列が `3, 20, 6` なので、アルファベットの前から何番目かで変換されてると予想できる。
* Flag
  * `PICOCTF{THENUMBERSMASON}`
  * なぜか全部大文字...
