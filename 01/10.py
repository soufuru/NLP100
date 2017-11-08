#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．

"""


# import sys
import fileinput

if __name__ == '__main__':
    # file = open(sys.argv[1], 'r')
    file = fileinput.input('-')

    count = 0
    for line in file:
        count += 1

    print(count)