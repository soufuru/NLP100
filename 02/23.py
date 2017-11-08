#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
23. セクション構造

記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

"""

import re
import fileinput

if __name__ == '__main__':

    for line in fileinput.input("-"):
        for text_line in line.split("\n"):
            m1 = re.match(r"(=+\s*)([^=\s]+)", text_line)
            if m1:
                print("　　" * (len(m1.group(1)) - 2) + str(m1.group(2)) + "(" + str(len(m1.group(1))-1) + ")")


