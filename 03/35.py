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
        for i in range(len(mlist)-1):
            # 名詞があったら
            if mlist[i]["pos"] == "名詞":
                # 「の」の前後の品詞を確認、両方共名詞なら抽出
                if mlist[i - 1]["pos"] == "名詞" and mlist[i + 1]["pos"] == "名詞":
                    print(mlist[i-1]["surface"] + "の" + mlist[i+1]["surface"])
