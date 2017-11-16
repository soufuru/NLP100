#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
37. 頻度上位10語

出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import fileinput
import re

if __name__ == '__main__':

    left = []
    height = []

    for file, num in zip(fileinput.input("-"), range(10)):
        m = re.match(r"(.*?)\t\:(.+)", file)
        if m:
            left.append(m.group(1))
            height.append(m.group(2))
            print(m.group())

    # フォントを日本語に変更
    plt.rcParams["font.family"] = "AppleGothic"
    plt.bar(np.array(left), np.array(height))
    plt.show()