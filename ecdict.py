#! /bin/python
# -*- conding: UTF-8 -*-

import csv
import sys
import subprocess
import textwrap as tp

tag = {'gk':'高','zk':'初','ky':'研','gre':'宝','ielts':'雅','toefl':'托','cet4':'四','cet6':'六'}
exg = {'p':'过去式','d':'过去分词','i':'现在分词','3':'第三人称','r':'比较级','t':'最高级','s':'复数','0':'原形'}
pos = {'a':'冠','c':'连','d':'限','i':'介','j':'形','m':'数','n':'名','p':'代','r':'副','u':'叹','t':'不','v':'动','x':'否'}

if __name__ == "__main__":
    with open('ecdict.csv') as f:
        with open('ecdict.txt', "w") as g:
            reader = csv.reader(f, delimiter=',')
            next(reader, None)
            for l in reader:
                g.write(':'+l[0]+':\n')
                if l[1] != '':
                    a = '[P] /' + l[1] + '/ '
                    if l[6] != '':
                        a += ' ⬥ '
                    if l[5] != '':
                        a += '★' * int(l[5]) + '☆' * (5 - int(l[5]))
                    if l[4] != '':
                        a +=  '  ' + ':'.join(map(lambda x:pos[x[0]] + x[2:], sorted(l[4].split('/'), key=lambda x:int(x[2:]), reverse=True)))
                    g.write(a+'\n')
                if l[3] != '':
                    a = '[T] ' + '\n    '.join(l[3].split('\\n'))
                    g.write(a.replace(' )',')').replace('( ', '(')+'\n')
                if l[2] != '':
                    a = list(filter(lambda x : x != '', l[2].replace('\\r','').replace('\\n ','').split('\\n')))
                    for i in range(len(a)):
                        b = '\n       '.join(list(tp.wrap(a[i][3:], 64)))
                        if i == 0:
                            b = '[D] ' + a[i][:3] + b
                        else:
                            b = '    ' + a[i][:3] + b
                        g.write(b + '\n')
                if l[10] != '':
                    a = list(filter(lambda x : x[0]!='1' and x[0]!='z' and x[0]!='b' and x[0]!='f',l[10].split('/')))
                    a = ''.join(map(lambda x:exg[x.split(':')[0]]+':'+x.split(':')[1]+'; ', a))
                    a = '[X] ' + '\n    '.join(list(tp.wrap(a, int(64*0.85))))
                    g.write(a + '\n')
                if l[7] != '':
                    a = ''.join(map(lambda x : tag[x], l[7].split(' ')))
                    if l[8] != '' or l[9] != '':
                        b = '-|' if l[8] == '' or l[8] == '0' else l[8]+'|'
                        b += '-' if l[9] == '' or l[9] == '0' else l[9]
                        if '-|-' not in b:
                            a += '  ' + b
                    g.write('[F] ' + a + '\n')
    subprocess.call('dictfmt --utf8 --allchars -s ECDICT -u https://github.com/skywind3000/ECDICT -j ecdict < ./ecdict.txt', shell=True)
    subprocess.call('dictzip ecdict.dict', shell=True)
#word,phonetic,definition,translation,pos,collins,oxford,tag,bnc,frq,exchange,detail,audio
