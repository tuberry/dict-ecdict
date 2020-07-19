#! /bin/python
# -*- conding: UTF-8 -*-

import csv
import subprocess

if __name__ == "__main__":
    with open("ecdict.csv") as f:
        with open("ecdicts.txt", "w") as g:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for l in reader:
                g.write(':'+l[0]+':\n')
                if l[3] != '':
                    a = '\n'.join(l[3].split('\\n'))
                    g.write(a.replace(' )',')').replace('( ', '(')+'\n')
    subprocess.call('dictfmt --utf8 --allchars -s ECDICTS -u https://github.com/skywind3000/ECDICT -j ecdicts < ./ecdicts.txt', shell=True)
    subprocess.call('dictzip ecdicts.dict', shell=True)
#word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
