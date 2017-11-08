#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ファイルのインポート リダイレクト

import fileinput

if __name__ == '__main__':

    # 標準入力から受け取ったファイルの一行目を出力

    # 引数の"-" : 標準入力から読み込む
    for line in fileinput.input('-'):

        # print(line.rstrip())
        print(line, end="")

        # ファイルに出力
        # print("aaaaa", file="")