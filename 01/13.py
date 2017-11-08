#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
13. col1.txtとcol2.txtをマージ
q
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

"""

import sys
# import fileinput

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as col1,  open(sys.argv[2], 'r') as col2:

        merge = ""

    # for line, filename in zip(fileinput.input(), fileinput.filename()):
    #     if fileinput.filename() != filename:
    #         print(filename)
    #         i += 1
    #     merge[i].append(line)
    # merge_file = open("merge.txt", "w")

        for line1, line2 in zip(col1.readlines(), col2.readlines()):
            merge += str(line1[0:-1]) + "\t" + str(line2[0:-1]) + "\n"

    print(merge)
