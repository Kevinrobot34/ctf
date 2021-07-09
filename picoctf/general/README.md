# General Skills

## Basic
### Obedient Cat
* Solution
  * ファイルをダウンロードするとFlagがあるだけ
* Flag
  * `picoCTF{s4n1ty_v3r1f13d_4a2b35fd}`
  * "sanity verified"
  * 最後のランダム文字列的なやつは、定期的に出題側が書き換えているっぽいやつ


### Lets Warm Up
* Solution
  ```bash
  $ python -c "print(bytes.fromhex('70'))"
  b'p'
  ```
* Flag
  * `picoCTF{p}`


### Warmed Up
* Solution
  ```bash
  $ python -c "print(0x3D)"
  61
  ```
* Flag
  * `picoCTF{61}`


### 2Warm
* Solution
  ```bash
  $ python -c "print(bin(42))"
  0b101010
  ```
* Flag
  * `picoCTF{101010}`


## Network関係
### what's a net cat?
* Solution
  * 以下のようにnetcatコマンドを使うだけ
    ```bash
    $ nc jupiter.challenges.picoctf.org 25103 
    ```
* Flag
  * `picoCTF{nEtCat_Mast3ry_d0c64587}`
  * "netcat mastery"


### Nice netcat...
* Solution
  * netcatで繋ぐと数字の羅列が出てくる
  * 明らかにasciiコードっぽいので、並べて見るだけ
* Flag
  * `picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8}`
  * "good kitty! nice kitty!"


### Magikarp Ground Mission
* Solution
  * sshしてinstanceに入って、置いてあるファイルを見ながらflagを探すだけ
* Flag
  * `picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}`


## Binary関係
### strings it
* Solution
  * 名前の通り、 `strings` コマンドをやってみるだけ
  * 出てくる情報が多いので `grep` かける
    ```bash
    $ strings ./strings | grep CTF
    YzOejwCTF3GVzbdb8PkOKp1cKvAwEUvRSOLLm1yFFETiT
    picoCTF{5tRIng5_1T_d66c7bb7}
    7Oqu9T7p8SAoQcOcQVHM46k1xpt1M6Iu2ag4dw1OFCTFRbv6
    ```
* Flag
  * `picoCTF{5tRIng5_1T_d66c7bb7}`
  * "Strings it"