#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
22. カテゴリ名の抽出

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re
import fileinput

if __name__ == '__main__':
    for line in fileinput.input("-"):
        for text_line in line.split("\n"):
            m = re.match("\[\[Category:(.*?)(?:\|.*)?\]\]", text_line)
            if m:
                print(m.group(1))

"""
メモ

(?:~)
~で指定した部分はマッチさせないし、groupにも属させない
(m.group(2)って書いたらエラー出た)
"""