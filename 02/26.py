#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
26. 強調マークアップの除去

25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．


"""

import re
import fileinput

if __name__ == '__main__':
    result = {}
    for file in fileinput.input("-"):
        # for line in file.split("\n"):
        #     m = re.match("(?:.*\|)?(.+)\s=\s(.+)", line)
        #
        #     # 25からの追加分
        #     tmp1 = ""
        #     tmp2 = ""
        #     if m:
        #         for i in str(m.group(1)):
        #             if i != "\'":
        #                 tmp1 += i
        #
        #         for j in str(m.group(2)):
        #             if j != "\'":
        #                 tmp2 += j
        #
        #         result.update({tmp1: tmp2})
        # 先生の
        b2 = re.compile("''(.+)''")
        b3 = re.compile("'''(.+)'''")
        b5 = re.compile("'''''(.+)'''''")

        # b5にマッチした部分をb5のgroup1に置き換え
        # 正規表現のキャプチャグループ
        r = b5.sub(r"\1", file.rstrip())
        r = b3.sub(r"\1", r)
        r = b2.sub(r"\1", r)
        print(r)

    # for key, obj in result.items():
    #     print("{0}, {1}".format(key, obj))



