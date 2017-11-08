#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""


import random

if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()

    lis = []

    for i in s:
        if len(i) > 4:
            tmp = list(i)

            # 先頭2番目から後ろから2番目の文字を取得
            rand_tmp = tmp[1:-1]

            # ランダムに並び替え
            random.shuffle(rand_tmp)

            result = tmp[0] + "".join(rand_tmp) + tmp[-1]
            lis.append(result)
        else:
            lis.append(i)

    print(lis)


