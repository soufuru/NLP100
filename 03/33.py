#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
33. サ変名詞

サ変接続の名詞をすべて抽出せよ．
"""

import fileinput

mlist_lib = __import__("30")

if __name__ == '__main__':

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for line in mlist:
            if line["pos1"] == "サ変接続":
                if line["surface"] != "——":
                    print(line["surface"])
