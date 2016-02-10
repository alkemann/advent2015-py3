#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def count_characters(s):
    code_count = len(s)

    encoded_count = len(s.replace("\"", "##").replace("\\", "##")) + 2

    characters = s[1:-1].replace("\\\\", "#").replace("\\\"", "#")
    char_count = len(re.sub("\\\\[x][\da-fA-F]{2}", "#", characters))

    return code_count, char_count, encoded_count


def total(strings):
    code_count = char_count = encoded_count = 0
    for s in strings:
        o, s, e = count_characters(s)
        code_count += o
        char_count += s
        encoded_count += e
    return code_count - char_count, encoded_count - code_count
