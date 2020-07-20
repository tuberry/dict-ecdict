# dict-ecdict
> A port of Ultimate [ECDICT] database for Dictd<br>
[![license]](/LICENSE)

![image](https://user-images.githubusercontent.com/17917040/87878103-c1ee5480-ca14-11ea-80a2-2f5322a43e01.png)

## Installation

### Requirements
1. curl
2. python3
3. dictd
4. make

### Build && Installation
```Makefile
make
sudo make install
```
Also, there is a simplified version:
```Makefile
make
sudo make install_simp
```
### Configuration
Add these lines below in `/etc/dict/dictd.conf`:
```dictdconf
database ecdict {
data /usr/share/dict/ecdict.dict.dz
index /usr/share/dict/ecdict.index
}
```
For the simplified version:
```dictdconf
database ecdicts {
data /usr/share/dict/ecdicts.dict.dz
index /usr/share/dict/ecdicts.index
}
```
Then restart `dictd.service`:
```shell
systemctl restart dictd
```

## Acknowledgements
1. [ECDICT](https://github.com/skywind3000/ECDICT-ultimate): Released under MIT license. All rights reserved by the author.
2. [dictd](https://en.wikipedia.org/wiki/DICT): Dict file format.
3. [fcitx5-pinyin-zhwiki](https://github.com/felixonmars/fcitx5-pinyin-zhwiki): Makefile.

[ECDICT]:https://github.com/skywind3000/ECDICT-ultimate
[license]:https://img.shields.io/badge/license-MIT-purple.svg
