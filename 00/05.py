#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

 05. n-gram
 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

"""


# 単語bi-gram
def voca_bigram(s):
    ss = s.split(" ")
    lis = []
    for i in range(len(ss) - 1):
        lis.append([ss[i], ss[i + 1]])
    return lis


# 文字bi-gram
def word_bigram(s):
    sss = list(s)
    lis = []

    for i in range(len(sss) - 1):
        lis.append(sss[i] + sss[i + 1])
    return lis



"""
    先生の答え
    (内包表記)

"""


def bigram(x):
    return [[x[i], x[i + 1]] for i in range(len(x) - 1)]


def ngram(x, n):
    return [x[i:i+n] for i in range(len(x) - n + 1)]


if __name__ == '__main__':
    s = "I am an NLPer"
    print(voca_bigram(s))
    print(word_bigram(s))


    ss = s.split()
    print(ngram(s,2))
    print(ngram(ss, 2))
