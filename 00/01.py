#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

if __name__ == '__main__':
    s = "パタトクカシーー"
    ss = ""

    # for i in range(8):
    #     if i % 2 == 1:
    #         ss += s[i]

# 文字列のスライス
    ss = s[::2]
    print(ss)


