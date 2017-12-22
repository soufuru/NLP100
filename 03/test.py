#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab
import fileinput

if __name__ == '__main__':
    s = "すもももももももものうち"
    parser = MeCab.Tagger()

    for m in parser.parse(s).split("\n"):
        print(m.split("\t")[0])
