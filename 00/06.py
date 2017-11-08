#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

  06. 集合
  "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

"""


def word_bigram(s):
    ss = list(s)
    lis = []
    # 空白を削除
    while " " in ss:
        ss.remove(" ")

    for i in range(len(ss)-1):
        lis.append(ss[i] + ss[i+1])
    return lis


if __name__ == '__main__':
    s = "paraparaparadise"
    ss = "paragraph"

    X = word_bigram(s)
    Y = word_bigram(ss)

    # XとYをリスト型からset型に変換
    x_set = set(X)
    y_set = set(Y)

    print("x_set : {0}".format(x_set))
    print("y_set : {0}\n".format(y_set))


    # 和集合
    print("和集合: {0} ".format(list(x_set | y_set)))
    # 積集合
    print("積集合: {0} ".format(list(x_set & y_set)))
    # 差集合
    print("差集合: {0} \n".format(list(x_set - y_set)))

    print("\"se\"という文字列はXに含まれているか? : {0}".format(str("se" in X)))
    print("\"se\"という文字列はYに含まれているか? : {0}".format(str("se" in Y)))


'''

set型(集合型)メモ

set型 : 集合を扱うための型。

set型とfrozenset型の2種類があり、set型は要素の変更が可能なのに対し、frozenset型は要素の変更が不可能。

リスト型との違い：
    ・要素の重複を許さない
    ・要素は順序付けされない

'''



