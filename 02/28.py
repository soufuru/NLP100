#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
28. MediaWikiマークアップの除去

27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

"""

import re
import fileinput

if __name__ == '__main__':
    result = {}
    for file in fileinput.input("-"):
        for line in file.split("\n"):
            m = re.match("(?:.*\|)?(.+)\s=\s(.+)", line)
            tmp1 = ""
            tmp2 = ""
            if m:
                for i in str(m.group(1)):
                    if i != "\'" and i != "[" and i != "]":
                        tmp1 += i

                for j in str(m.group(2)):
                    if j != "\'" and j != "[" and j != "]":
                        tmp2 += j

                result.update({tmp1: tmp2})

    for key, obj in result.items():
        print("{0}, {1}".format(key, obj))


