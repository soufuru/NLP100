#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
25. テンプレートの抽出

記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import re
import fileinput

if __name__ == '__main__':
    result = {}
    for file in fileinput.input("-"):
        for line in file.split("\n"):
            m = re.match("(?:.*\|)?(.+)\s=\s(.+)", line)
            if m:
                result.update({m.group(1): m.group(2)})

    for key, obj in result.items():
        print("{0}, {1}".format(key, obj))
