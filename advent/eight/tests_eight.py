from unittest import TestCase
from advent.eight.eight import *

"""

"" is 2 characters of code (the two double quotes),
 but the string contains zero characters.

"abc" is 5 characters of code, but 3 characters in the string data.

"aaa\"aaa" is 10 characters of code, but the string itself contains
 six "a" characters and a single, escaped quote character, for a total
 of 7 characters in the string data.

"\x27" is 6 characters of code, but the string itself contains
 just one - an apostrophe ('), escaped using hexadecimal notation.

"""


class TestEight(TestCase):
    def test_counting(self):
        code_count, char_count, encoded_count = count_characters("\"\"")
        self.assertEqual(0, char_count)
        self.assertEqual(6, encoded_count)
        self.assertEqual(2, code_count)

        code_count, char_count, encoded_count = count_characters("\"abc\"")
        self.assertEqual(3, char_count)
        self.assertEqual(9, encoded_count)
        self.assertEqual(5, code_count)

        code_count, char_count, encoded_count = count_characters("\"aaa\\\"aaa\"")
        self.assertEqual(7, char_count)
        self.assertEqual(16, encoded_count)
        self.assertEqual(10, code_count)

        code_count, char_count, encoded_count = count_characters("\"\\x27\"")
        self.assertEqual(1, char_count)
        self.assertEqual(11, encoded_count)
        self.assertEqual(6, code_count)

    def test_total(self):
        strings = [
            "\"\"",
            "\"abc\"",
            "\"aaa\\\"aaa\"",
            "\"\\x27\""
        ]
        expected_char = (2+5+10+6)-(0+3+7+1)  # 12
        expected_encoded = (6+9+16+11)-(2+5+10+6) # 19
        result_char, result_encoded = total(strings)
        self.assertEqual(expected_char, result_char)
        self.assertEqual(expected_encoded, result_encoded)
