#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

"""

import fileinput
from collections import Counter

if __name__ == '__main__':
    counter = Counter()

    with fileinput.input('-') as list:
        for i in list:
            col = i.split()
            counter[col[0]] += 1

            # counterは

    for result,count in counter.most_common():
        print(result, count)



# メモ
"""
リストの変数名は英単語の複数形にするか、~listと命名するほうがよい

"""