#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

"""


import sys
import fileinput

if __name__ == '__main__':

    # file = open(sys.argv[1], 'r')
    file = fileinput.input("-")

    for line in file:
        lis = list(line)

        # for tab, i in zip(lis, range(len(lis))):
        #     # タブを空白に変換
        #     if tab == "\t":
        #         lis[i] = " "
        #     result = "".join(lis)

        # 内包表記
        result = "".join([" " if lis[i] == "\t" else lis[i] for i in range(len(lis))])

        print(result, end='')
        # print(line)