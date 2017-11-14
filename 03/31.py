#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
31. 動詞

動詞の表層形をすべて抽出せよ．
"""

import fileinput
import re
teacher = __import__("teacher_30")

if __name__ == '__main__':

    for mlist in teacher.to_mlist(fileinput.input("-")):
        for line in mlist:
            m = re.search(r"'surface': '(.+?)'.*'pos': '動詞'", str(line))
            if m:
                print(m.group(1))
