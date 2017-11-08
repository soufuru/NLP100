#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

"""

import fileinput
import json

if __name__ == '__main__':
    for line in fileinput.input("-"):
        obj = json.loads(line)
        if obj["title"] == "イギリス":
            print(obj["text"], end='')
            break





"""
JSON形式

{
    "name" : "yaju_senpai",
    "age"  : "810"
    "array" : [1, 2, 3]

}


"""