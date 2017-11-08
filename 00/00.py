#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．


#文字列は文字の配列として扱える


if __name__ == '__main__':
    s = "stressed"
    print("s = {0}".format(s))
    # a = 2
    # b = 3
    # print("{0} , {1}".format(a,b))

# 変数ssにsを逆に並べた文字列を代入する.
    ss = s[::-1]
    print("ss = {0}".format(ss))

#
# スライス
#

# 0から(3-1)番目までの要素を取り出す
    ss = s[0:3]
    print("ss = {0}".format(ss))

    ss = s[:3]
    print("ss = {0}".format(ss))

# 0番目から2文字ずつ(0,2,4,6,8,...)番目を表示
    ss = s[::2]
    print("ss = {0}".format(ss))

# print関数はデフォルトで改行(最後に\nが挿入される)されてしまう
# "end"オプションで最後の文字を設定できるので、end=''とすれば改行なしのprintができる

