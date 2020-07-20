#! /bin/python
# -*- conding: UTF-8 -*-

import csv
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        with open(sys.argv[2], "w") as g:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for l in reader:
                g.write(':'+l[0]+':\n')
                if l[3] != '':
                    a = '\n'.join(l[3].split('\\n'))
                    g.write(a.replace(' )',')').replace('( ', '(')+'\n')
#word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
