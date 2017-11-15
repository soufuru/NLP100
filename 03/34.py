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
            m = repatter1.search(str(line))
            if m:
                # 「の」の前後の品詞を確認、両方共名詞なら抽出
                m1 = repatter2.search(str(mlist[i-1]))
                m2 = repatter2.search(str(mlist[i+1]))

                if m1 and m2:
                    print(m1.group(1) + "の" + m2.group(1))
