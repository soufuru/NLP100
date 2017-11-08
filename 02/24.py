#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
24. ファイル参照の抽出

記事から参照されているメディアファイルをすべて抜き出せ．

"""

import re
import fileinput

if __name__ == '__main__':

    for file in fileinput.input("-"):
        for line in file.split("\n"):
            m = re.match("(?:.*\[\[)?(?:File|ファイル):([^|]*)", line)
            if m:
                print(m.group(1))


