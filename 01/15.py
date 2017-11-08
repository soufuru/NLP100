#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

"""

import sys
import fileinput

# 自分の解答 ・・・　イケてない
#
# if __name__ == '__main__':
#     file = fileinput.input("-")
#     num = int(sys.argv[1])
#
#     tmp = []
#     array = []
#
#     for line in file:
#         tmp.append(line)
#
#     tmp.reverse()
#
#     for i in range(num):
#         array.append(tmp[i])
#
#     array.reverse()
#
#     for i in range(num):
#         print(array[i], end="")


# けんの解答
"""

    n = int(sys.argv[1])
    with open('hightemp.txt','r') as f:
        
        lines = f.readlines()[-n:] 
        
        #readlinesはファイルサイズがでかすぎると終わる
    
    result = "¥n".join([line.rstrip() for line in lines])
    print(result)


"""

# 先生の板書

"""
    
    例えば: 後ろから五行欲しい
    
    要素数5の配列を用意
    前から詰めていき、古いものは配列の後ろにずらしていく。要素数が5を超えたものは古いものから捨てていく。(データアルゴでやった"キュー"のこと)
    
"""

# 先生の解答 : queueを使ったもの。ファイルのサイズに制約がない

from collections import deque

if __name__ == '__main__':
    num = int(sys.argv[1])
    # maxlen : 長さ限定のキューを作る
    d = deque(maxlen=num)

    for line in fileinput.input('-'):
        d.appendleft(line.rstrip())

    for line in reversed(d):
        print(line)




