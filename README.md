# dict-ecdict

A port of Ultimate [ECDICT] database for Dictd
>.<br>
[![license]](/LICENSE)

![image](https://user-images.githubusercontent.com/17917040/87878103-c1ee5480-ca14-11ea-80a2-2f5322a43e01.png)

## Installation

### Requirements

1. curl
2. python3
3. dictd
4. make

### Build && Install

```bash
make # FULL=true
sudo make install
```

Also it's avaliable in [AUR](https://aur.archlinux.org/packages/dict-ecdict-git/):

```bash
yay -S dict-ecdict-git
```

### Configuration

Add these lines below in `/etc/dict/dictd.conf`:

```conf
database ecdict {
data /usr/share/dict/ecdict.dict.dz
index /usr/share/dict/ecdict.index
}
```

Then restart `dictd.service`:

```bash
systemctl restart dictd
```

## Acknowledgements

1. [ECDICT]: Released under MIT license. All rights reserved by the author.
2. [dictd](https://en.wikipedia.org/wiki/DICT): Dict file format.

[ECDICT]:https://github.com/skywind3000/ECDICT-ultimate
[license]:https://img.shields.io/badge/license-MIT-purple.svg
