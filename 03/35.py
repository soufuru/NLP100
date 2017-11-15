#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
35. 名詞の連接

名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import re
import fileinput

mlist_lib = __import__("30")

if __name__ == '__main__':

    pattern1 = r"'surface': '(.+?)', 'base': '(?:.+?)', 'pos': '名詞'"
    repatter1 = re.compile(pattern1)

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        tmp = ""
        for line in mlist:
            # 名詞があったら

            print(line["pos"])

            # m = repatter1.search(str(line))
            # if m:


