#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

if __name__ == '__main__':
    e = "パトカー"
    f = "タクシー"
    g = ""

    # for i in range(4):
    #     g += e[i]
    #     g += f[i]

# (a, b)という書き方はタプル型
    for (a, b) in zip(e, f):
        g += a + b

# 内包表記
    
    print(g)
