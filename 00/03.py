#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

"""
import re

if __name__ == '__main__':
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

    # スペースで文字を区切り、区切った文字のリストを作成
    # ss = s.split(" ")

    # 結果
    # [3, 1, 4, 1, 6, 9, 2, 7, 5, 3, 5, 8, 9, 7, 10]
    # ----→ カンマも文字数としてカウントされてしまう

    # 「re」モジュールを入れてみる
    #  「,」と「　」で分割し、リストを作成
    ss = re.split(',| |\.', s)

    # 結果
    # [3, 1, 4, 1, 5, 0, 9, 2, 6, 0, 5, 3, 5, 8, 9, 7, 9]
    # -----→「,」と「 」が連続するところもリストに含まれてしまうので、if文で除去

    lis = []

    # for i in range(len(ss)):
    #     if len(ss[i]) != 0:
    #         lis.append(len(ss[i]))

    # 内包表記
    l = s.split()
    lis = [len(w.strip(':,.')) for w in l]


    # print(ss)
    print(l)
    print(lis)

