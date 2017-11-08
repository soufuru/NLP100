#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""
import sys
import fileinput

if __name__ == '__main__':
    # hightemp = open(sys.argv[1], 'r')
    hightemp = fileinput.input("-")

    col1 = []
    col2 = []

    for line in hightemp:
        lis = list(line)

        # 内包表記
        result = "".join([" " if lis[i] == "\t" else lis[i] for i in range(len(lis))]).split()

        col1.append(result[0])
        col2.append(result[1])

    # print(str("\n".join(col1)) + "\n")
    # print(str("\n".join(col2)) + "\n")

    with open("col1.txt", "w") as file1:
        file1.write(str("\n".join(col1)) + "\n")

    with open("col2.txt", "w") as file2:
        file2.write(str("\n".join(col2)) + "\n")

