from unittest import TestCase
from five import *


class TestFive(TestCase):
    def test_is_bad(self):
        # ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
        # aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
        self.assertTrue(is_nice("aaa"))
        # jchzalrnumimnmhp is naughty because it has no double letter.
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
        # haegwjzuvuyypxyu is naughty because it contains the string xy.
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
        # dvszwmarrgswjxmb is naughty because it contains only one vowel.
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))

    def test_improved(self):
        # qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
        self.assertTrue(is_nice_improved("qjhvhtzxzqqjkmpb"))
        # xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
        self.assertTrue(is_nice_improved("xxyxx"))
        # uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
        self.assertFalse(is_nice_improved("uurcxstgmygtbstg"))
        # ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
        self.assertFalse(is_nice_improved("ieodomkazucvgmuy"))
