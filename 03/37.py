#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
37. 頻度上位10語

出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import fileinput
import re

import matplotlib.pyplot as plt
import matplotlib.font_manager

if __name__ == '__main__':

    left = []
    height = []

    for file, num in zip(fileinput.input("-"), range(10)):
        print(file)
        m = re.match(r"(.*?)\t\:(.+)", file)
        if m:
            left.append(m.group(1))
            height.append(int(m.group(2)))

    # フォントを日本語に変更
    plt.rcParams["font.family"] = "AppleGothic"
    fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Arial Unicode.ttf")

    # y軸の範囲を設定
    plt.ylim([3000, 10000])

    # x軸のラベルを無理やり設定
    plt.xticks(range(10), left)

    # 棒グラフを生成
    plt.bar(range(10), height)

    # 棒グラフに値を設定
    for x, y in zip(range(10), height):
        plt.text(x, y, y, ha='center', va='bottom')


    # グラフの体裁を整える
    plt.title(u"「吾輩は猫である」頻出上位10単語", fontdict={"fontproperties": fontprop})
    plt.xlabel(u"単語", fontdict={"fontproperties": fontprop})
    plt.ylabel(u"出現数", fontdict={"fontproperties": fontprop})


    # 表示
    plt.show()
