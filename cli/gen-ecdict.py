#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
import argparse
import textwrap as tp

tag = {'gk':'高','zk':'初','ky':'研','gre':'宝','ielts':'雅','toefl':'托','cet4':'四','cet6':'六'}
exg = {'p':'过去式','d':'过去分词','i':'现在分词','3':'第三人称','r':'比较级','t':'最高级','s':'复数','0':'原形'}
pos = {'a':'冠','c':'连','d':'限','i':'介','j':'形','m':'数','n':'名','p':'代','r':'副','u':'叹','t':'不','v':'动','x':'否'}

def main():
    args = parser()
    if args.mini:
        ecdicts(args.input, args.output)
    else:
        ecdict(args.input, args.output)

def parser():
    agp = argparse.ArgumentParser()
    agp.add_argument('-i', '--input', help='specify the input file')
    agp.add_argument('-o', '--output', help='specify the output file')
    agp.add_argument('-m', '--mini', default=True, action=argparse.BooleanOptionalAction,
                     help='keep words and their definitions only')
    return agp.parse_args()

def ecdicts(ifile, ofile):
    with open(ifile) as f:
        with open(ofile, "w") as g:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for l in reader:
                if ' ' in l[0]: continue # ignore all phrases
                g.write(':'+l[0]+':\n')
                if l[3]: g.write('\n'.join(l[3].split('\\n')).replace(' )',')').replace('( ', '(')+'\n')

#word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
def ecdict(ifile, ofile):
    with open(ifile) as f:
        with open(ofile, "w") as g:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for l in reader:
                g.write(':'+l[0]+':\n')
                if l[1]:
                    a = '[P] /' + l[1] + '/ '
                    if l[6]: a += ' ⬥ '
                    if l[5]: a += (lambda x: '★' * x + '☆' * (5 - x))(int(l[5]))
                    if l[4]: a +=  '  ' + ':'.join(map(lambda x: pos[x[0]] + x[2:], sorted(l[4].split('/'), key=lambda x: int(x[2:]), reverse=True)))
                    g.write(a + '\n')
                if l[3]:
                    a = '[T] ' + '\n    '.join(l[3].split('\\n'))
                    g.write(a.replace(' )',')').replace('( ', '(')+'\n')
                if l[2]:
                    a = list(filter(lambda x: x != '', l[2].replace('\\r','').replace('\\n ','').split('\\n')))
                    for i in range(len(a)):
                        g.write(('[D] ' if i == 0 else '    ') + a[i][:3] + '\n       '.join(list(tp.wrap(a[i][3:], 64))) + '\n')
                if l[10]:
                    a = list(filter(lambda x: x[0] != '1' and x[0] != 'z' and x[0] != 'b' and x[0] != 'f', l[10].split('/')))
                    a = ''.join(map(lambda x: exg[x.split(':')[0]] + ':' + x.split(':')[1] + '; ', a))
                    g.write('[X] ' + '\n    '.join(list(tp.wrap(a, int(64 * 0.85)))) + '\n')
                if l[7]:
                    a = ''.join(map(lambda x : tag[x], l[7].split(' ')))
                    if (lambda x: x and int(x) != 0)(l[8] + l[9]):
                        a += (lambda x, y, f: f(x) + '|' + f(y))(l[8], l[9], lambda z: ('' if z == '0' else z) or '-')
                    g.write('[F] ' + a + '\n')

if __name__ == "__main__":
    main()
