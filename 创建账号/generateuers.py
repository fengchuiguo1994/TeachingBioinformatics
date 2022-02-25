# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:29:48 2021

@author: huang
"""

from xpinyin import Pinyin
import sys

p = Pinyin()
fin = open(sys.argv[1],encoding="utf8")
fout = open(sys.argv[2],"w")
myset = set()
for line in fin:
    tmp = line.strip().split()
    if len(tmp) != 2:
        sys.exit("error!")
    tmp[0] = tmp[0].strip()
    tmp[1] = tmp[1].strip()
    tmp[1] = "{0}{1}".format(tmp[1][1:],tmp[1][0])
    # print(tmp[0])
    # print(tmp[1])
    ret = p.get_pinyin(tmp[1])
    tmppy = ret.split("-")
    mystrlist = []
    for ii in tmppy[:-1]:
        mystrlist.append(ii[0])
    mystrlist.append(tmppy[-1])
    username = "".join(mystrlist)
    password = "{0}_{1}".format(username,tmp[0][-6:])
    # print(tmp[0])
    # print(tmp[1])
    if username not in myset:
        myset.add(username)
    else:
        sys.stderr.write("{0}\n".format(username))
    fout.write("{0}\t{1}\n".format(username,password))
fin.close()    
fout.close()