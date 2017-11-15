#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
32. 動詞の原形

動詞の原形をすべて抽出せよ．
"""

import fileinput

mlist_lib = __import__("30")

if __name__ == '__main__':

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for line in mlist:
            if line['pos'] == '動詞':
                print(line['base'])
