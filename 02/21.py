#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ
"""


import re
import json
import fileinput

if __name__ == '__main__':
    for line in fileinput.input("-"):
        obj = json.loads(line)
        for text_line in obj["text"].split("\n"):
            m = re.match("\[\[Category:(.+)\]\]", text_line)
            if m:
                print(text_line)

