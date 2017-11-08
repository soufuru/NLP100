#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
16. ファイルをN分割する


自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

"""

# import sys, fileinput
#
# if __name__ == '__main__':
#     # file = open(sys.argv[1], 'r')
#     file = fileinput.input("-")
#     num = int(sys.argv[1])
#
#     array = []
#     tmp = []
#
#     for line in file:
#         array.append(line)
#
#     i = 0
#     while True:
#         tmp.append(array[i:i+num])
#         i += num
#         if i == len(array):
#             break
#
#     print(tmp)


import sys
import math

fname = 'hightemp.txt'
n = int(sys.argv[1])

with open(fname) as data_file:
    lines = data_file.readlines()

count = len(lines)
unit = math.ceil(count / n)  # 1ファイル当たりの行数

# enumerate(iterable, start)
# range(start, stop, step)

for i, offset in enumerate(range(0, count, unit), 1):
    with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
        for line in lines[offset:offset + unit]:
            out_file.write(line)



# メモ

"""
    巨大ファイルを読み込むためには

    一回ファイルを読み込み、行数をカウントしてから、それ相応の配列を用意し、
    もう一度ファイルを読み込めば、巨大なファイルもイケるはず。
    2回ファイルを読み込むので、ファイルがでかければそれなりに時間がかかる。


"""


