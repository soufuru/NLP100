#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
38. ヒストグラム

単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け

"""

import fileinput
import re

import matplotlib.font_manager
import matplotlib.pyplot as plt

if __name__ == '__main__':

    left = []
    height = []

    for file in fileinput.input("-"):
        m = re.match(r"(.*?)\t\:(.+)", file)
        if m:
            left.append(m.group(1))
            height.append(int(m.group(2)))

    for i in range(20):
        print(str(left[i]) + ":" + str(height[i]))

    # フォントを日本語に変更
    plt.rcParams["font.family"] = "AppleGothic"
    fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Arial Unicode.ttf")

    # x軸の範囲を設定
    plt.xlim(xmin=1, xmax=20)

    # y軸の範囲を設定
    plt.ylim([0, 7000])

    # x軸のラベルを無理やり設定
    plt.xticks(range(1, 20), range(1, 20))

    # ヒストグラムを生成
    plt.hist(height, bins=20, range=(1, 20))

    # グラフの体裁を整える
    plt.title(u"ヒストグラム", fontdict={"fontproperties": fontprop})
    plt.xlabel(u"単語", fontdict={"fontproperties": fontprop})
    plt.ylabel(u"出現数", fontdict={"fontproperties": fontprop})

    # ヒストグラム表示
    plt.show()
