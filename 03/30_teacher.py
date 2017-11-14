#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput
from typing import Iterable


def to_mlist(lines: Iterable[str]):
    mlist = []
    for line in lines:
        s = line.rstrip()
        if s == 'EOS':
            ret = mlist
            mlist = []
            yield ret
        else:
            surface, feature_str = s.split("\t")
            features = feature_str.split(",")
            mlist.append({
                "surface": surface,
                "base": features[6],
                "pos": features[0],
                "pos1": features[1]
            })


if __name__ == '__main__':
    for mlist in to_mlist(fileinput.input("-")):
        print(mlist)

