#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
31. 動詞

動詞の表層形をすべて抽出せよ．
"""

import fileinput
import re
mlist_lib = __import__("30")

if __name__ == '__main__':

    pattern = r"'surface': '(.+?)'.*'pos': '動詞'"
    repatter = re.compile(pattern)

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for line in mlist:
            m = repatter.search(str(line))
            if m:
                print(m.group(1))
