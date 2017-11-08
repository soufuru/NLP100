#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 　外延敵表記 ・・・ 具体的な数値を書く
    a1 = [1, 3, 5, 7, 9]

    # 　内包的表記 ・・・　
    a2 = [n for n in range(10) if n % 2 != 0]

    # 情報数学で習った書き方
    # {x | xは奇数、0 <= x <= 10}

    # Pythonだと
    # | = for

    print(a1)
    print(a2)

    b1 = [1, 4, 9, 16, 25, 36]
    b2 = [n * n for n in range(1, 7)]

    print(b1)
    print(b2)



    str = "ab cd ef gh"
    str2 = str.split()
    print(str2[2][:1])


