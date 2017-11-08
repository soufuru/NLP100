#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine.
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ.

"""

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# ss = re.split(" ", s)
ss = s.split(" ")


dic = {}
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for string, number in zip(ss, range(len(ss))):
    if number+1 in one:
        dic.update({string[0]: number+1})
    else:
        dic.update({string[0]+string[1]: number+1})

# 先生のやり方
# def getlen(num):
#     one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
#     if num in one:
#         return 1
#     else:
#         return 2
#
#
# dict = {i + 1: ss[i][0:getlen(i + 1)] for i in range(len(ss))}
# print(dict)

print(dic)
print(dic["He"])
