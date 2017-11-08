#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
27. 内部リンクの除去

26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

"""

import re
import fileinput

if __name__ == '__main__':
    # result = {}

    p1 = re.compile(r"\[\[(^[\]]+)\]\]")
    p2 = re.compile(r"\[\[[^[|\]]+\|(.+)\]\]")

    for file in fileinput.input("-"):
        r = p2.sub("\1", file.rstrip())
        r = p1.sub("\1", r)

        print(r)


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



