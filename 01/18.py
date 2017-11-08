#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
18. 各行を3コラム目の数値の降順にソート

各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

"""

import fileinput

if __name__ == '__main__':

    dictionary = {}

    file = fileinput.input('-')
    for line in file:
        tmp = line.split()
        dictionary.update({tmp[2]: line})


    dictionary = reversed(sorted(dictionary.items()))

    for txt in dictionary:
        print(txt[1], end='')



