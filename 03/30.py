#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

先生メモ

表層系・・・入力文に現れたものそのもの mecabの出力の一番左
基本形・・・終止形。「あっ(た)→ある」
品詞
品詞細分類・・・名詞 → 一般名詞、代名詞、等

解析結果 カンマ区切り
0 品詞
1~5 品詞細分類
6 基本形
7

"""

import fileinput
import re

if __name__ == '__main__':
    lis = [{}]
    i = 0

    for file in fileinput.input("-"):
        m = re.match(r'EOS', file)
        if m:
            lis.append({})
            i += 1
        else:
            line = re.split(r'[,\t\n]', file)
            lis[i].update({"surface": line[0],
                           "pos": line[1],
                           "pos1": line[2],
                           "base": line[7]}
                          )

    print(lis)
