## picoCTF / crypto
### Mod 26
* Solution
  * ROT13やるだけ
  * 自分で組んでも良いし、コマンド叩いても良い
* Flag
  * `picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}`
  * "Next time I'll try to rounds of rot13"
  * 最後のランダム文字列的なやつは、定期的に出題側が書き換えているっぽいやつ


### The Numbers
* Solution
  * 画像を見ると明らかにFlagっぽい文字列が数字に変換されて並んでいる
  * CTFに相当しそうな文字列が `3, 20, 6` なので、アルファベットの前から何番目かで変換されてると予想できる。
* Flag
  * `PICOCTF{THENUMBERSMASON}`
  * なぜか全部大文字...


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
    * 問題名になぞらえたflag
  * 最後の `_` 以降は定期的に出題側が書き換えているっぽいやつ