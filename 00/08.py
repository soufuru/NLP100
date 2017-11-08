#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

# 英小文字のAsciiコードは97 - 122


def cipher(string: str) -> str:
    result = ""
    # for s in string:
    #     if ord(s) in range(97, 123): #ord : 文字コードに変換
    #         result += chr(219 - ord(s))
    #     else:
    #         result += s

    # 三項演算子
    result = "".join([chr(219-ord(s)) if ord(s) in range(97, 123) else s for s in string])

    return result


if __name__ == '__main__':

    sentence = "I am a Fukuoka University student. This is a test sentence."

    # 暗号化
    encryption = cipher(sentence)
    print(encryption)

    # 復号化
    decription = cipher(encryption)
    print(decription)


