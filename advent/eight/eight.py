#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def count_characters(s):
    """
    Returns two values, first being the code count, the second the char count
    :param s: string
    :return: int, int
    """
    code_count = len(s)
    s = s[1:-1]
    s = s.replace("\\\\", "#")
    s = s.replace("\\\"", "#")
    s = re.sub("\\\\[x][\da-fA-F]{2}", "#", s)
    char_count = len(s)
    return code_count, char_count


def total(strings):
    """
    Calculates all all code lengths of strings and all character counts
     and returns code - char
    :param strings: list of strings
    :return: int
    """
    code_count = char_count = 0
    for s in strings:
        o,s = count_characters(s)
        code_count += o
        char_count += s
    return code_count - char_count


def count_encoded_characters(s):
    """
    count code length and count length of encoded string
    :param s: string
    :return: int, int
    """
    code_count = len(s)
    s = s.replace("\"", "##")
    s = s.replace("\\", "##")

    encoded_count = len(s) + 2
    return code_count, encoded_count


def total_encoded(strings):
    """
    Calculates all all code lengths of strings and all encoundet counts
     and returns encoded - code
    :param strings: list of strings
    :return: int
    """
    code_count = encoded_count = 0
    for s in strings:
        o, e = count_encoded_characters(s)
        code_count += o
        encoded_count += e
    return encoded_count - code_count

