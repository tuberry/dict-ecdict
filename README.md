# dict-ecdict

A port of Ultimate [ECDICT] database for Dictd
>.<br>
[![license]](/LICENSE.md)

![image](https://user-images.githubusercontent.com/17917040/87878103-c1ee5480-ca14-11ea-80a2-2f5322a43e01.png)

## Dependencies

* curl (make)
* make (make)
* unzip (make)
* python (make)
* dictd (depend/make)

## Installation

```bash
make && sudo make install
```

## [AUR](https://aur.archlinux.org/packages/dict-ecdict-git/)

```bash
yay -S dict-ecdict-git # for Arch-based distros
```

## Configuration

Add these lines below to `/etc/dict/dictd.conf`:

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

* [dictd]: DICT file format
* [ECDICT]: released under MIT license, all rights reserved by the author

[dictd]:https://en.wikipedia.org/wiki/DICT
[ECDICT]:https://github.com/skywind3000/ECDICT-ultimate
[license]:https://img.shields.io/badge/license-MIT-purple.svg
