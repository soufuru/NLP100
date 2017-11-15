#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
34. 「AのB」

2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import fileinput
mlist_lib = __import__("30")


if __name__ == '__main__':

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for i in range(len(mlist)-1):
            # 助詞の「の」があったら
            if mlist[i]["pos"] == "助詞" and mlist[i]["base"] == "の":
                # 「の」の前後の品詞を確認、両方共名詞なら抽出
                if mlist[i - 1]["pos"] == "名詞" and mlist[i + 1]["pos"] == "名詞":
                    print(mlist[i-1]["surface"] + "の" + mlist[i+1]["surface"])


