#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
27. 内部リンクの除去

26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

"""

import re
import fileinput

if __name__ == '__main__':

    # p1 = re.compile(r"\[\[([^\[\]]+)\]\]")
    p1 = re.compile(r".*?\[\[(.+)\]\]")
    p2 = re.compile(r".*?\[\[[^\[\]]+\|(.+?)\]\]")

    for line in fileinput.input("-"):

        r = re.match(p1, line)
        if r:
            r1 = re.match(p2, r.group())
            if r1:
                print(r1.group(1))
            else:
                print(r.group(1))
        # r1 = p2.sub("\1", line.rstrip())
        # r = p1.sub("\1", r1)

        # print(line)



    # result = {}
    #     for line in file.split("\n"):
    #         m = re.match("(?:.*\|)?(.+)\s=\s(.+)", line)
    #         tmp1 = ""
    #         tmp2 = ""
    #         if m:
    #             m2 = re.match(r"[^\[\]]*", m.group(1))
    #             if m2:
    #                 tmp1 = m2.group()
    #
    #             print(m.group(2))
    #             m2 = re.match(r"(.[^\[\]'])*", m.group(2))
    #             if m2:
    #                 tmp2 = m2.group()
    #                 print(m2.group())
    #
    #             result.update({tmp1: tmp2})
    #
    # for key, obj in result.items():
    #     print("{0}, {1}".format(key, obj))



