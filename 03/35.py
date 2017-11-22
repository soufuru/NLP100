#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
35. 名詞の連接

名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import fileinput
mlist_lib = __import__("30")


if __name__ == '__main__':

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        tmp = []
        for i in range(len(mlist)-1):
            # 名詞があったら
            if mlist[i]["pos"] == "名詞":
                tmp.append(mlist[i]["surface"])
            else:
                if len(tmp) != 0:
                    print("".join(tmp))
                tmp = []

