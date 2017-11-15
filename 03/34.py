#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
34. 「AのB」

2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import re
import fileinput

mlist_lib = __import__("30")

if __name__ == '__main__':

    pattern1 = r"'surface': 'の', 'base': 'の', 'pos': '助詞', 'pos1': '連体化'"
    pattern2 = r"'surface': '(.+?)', 'base': '(?:.+?)', 'pos': '名詞'"
    repatter1 = re.compile(pattern1)
    repatter2 = re.compile(pattern2)

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for i, line in enumerate(mlist):
            # 助詞の「の」があったら
            if line["pos"] == "助詞" and line["base"] == "の":
                # 「の」の前後の品詞を確認、両方共名詞なら抽出
                if mlist[i-1]["pos"] == "名詞" and mlist[i+1]["pos"] == "名詞":
                    # print(mlist[i-1]["surface"] + "の" + mlist[i+1]["surface"])
                    print(mlist)
