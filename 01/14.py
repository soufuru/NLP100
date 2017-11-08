#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
14. 先頭からN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

"""

import sys
import fileinput

if __name__ == '__main__':

    num = int(sys.argv[1])

    # 標準入力を使うときは閉じないほうが良い
    with fileinput.input("-") as file:

    # file = fileinput.input("-")
        for _ in range(num):
            print(file.readline(), end="")


    # 先生の解答
    # enumerate
    for i, line in enumerate(fileinput.input('-')):
        if i >= num:
            break
        print(line.rstrip())


