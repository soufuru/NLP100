#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
17. １列目の文字列の異なり

1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

"""

import fileinput

if __name__ == '__main__':

    file = fileinput.input('-')
    str_set = set()

    for line in file:
        tmp = line.split()
        str_set.add(tmp[0])


    for string in str_set:
        print(string)



