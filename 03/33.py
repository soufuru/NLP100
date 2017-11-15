#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
33. サ変名詞

サ変接続の名詞をすべて抽出せよ．
"""

import re
import fileinput

mlist_lib = __import__("30")

if __name__ == '__main__':

    pattern = r"'surface': '(.+?)', 'base': '(?:.+?)', 'pos': '名詞', 'pos1': 'サ変接続'"
    repatter = re.compile(pattern)

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for line in mlist:
            m = repatter.search(str(line))
            if m:
                if m.group(1) != "——":
                    print(m.group(1))
