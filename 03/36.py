#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
36. 単語の出現頻度

文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import fileinput
mlist_lib = __import__("30")


if __name__ == '__main__':

    dictionary = {}

    for mlist in mlist_lib.to_mlist(fileinput.input("-")):
        for i in range(len(mlist)):
            if mlist[i]["surface"] in dictionary.keys():
                dictionary[mlist[i]["surface"]] += 1
            else:
                dictionary.update({mlist[i]["surface"]: 1})

    # value(単語の出現数)でソート
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]):
        print(key + "\t:" + str(value))

