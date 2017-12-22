#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
39. Zipfの法則

単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import fileinput
import matplotlib.pyplot as plt
import matplotlib.font_manager
import re

if __name__ == '__main__':

    left = []
    height = []

    for file in fileinput.input("-"):
        m = re.match(r"(.*?)\t\:(.+)", file)
        if m:
            left.append(m.group(1))
            height.append(int(m.group(2)))


    # フォントを日本語に変更
    plt.rcParams["font.family"] = "AppleGothic"
    fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/Arial Unicode.ttf")

    # y軸の範囲を設定
    # plt.ylim([0, 7000])

    # x軸のラベルを無理やり設定
    # plt.xticks(range(1, 20), range(1, 20))

    # height = [height[i] for i in range(20)]

    # 両対数グラフを生成
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(height, range(len(height)))

    # グラフの体裁を整える
    plt.title(u"両対数グラフ", fontdict={"fontproperties": fontprop})
    plt.xlabel(u"単語", fontdict={"fontproperties": fontprop})
    plt.ylabel(u"出現数", fontdict={"fontproperties": fontprop})

    # 両対数グラフを表示
    plt.show()
