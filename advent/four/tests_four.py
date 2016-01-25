from unittest import TestCase
from four import mine


class TestMine(TestCase):
    def test_mine(self):
        # If your secret key is abcdef, the answer is 609043,
        # because the MD5 hash of abcdef609043 starts with five
        # zeroes (000001dbbfa...), and it is the lowest such number to do so.
        self.assertEqual(609043, mine("abcdef"))

        # If your secret key is pqrstuv, the lowest number it combines with
        # to make an MD5 hash starting with five zeroes is 1048970;
        # that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
        self.assertEqual(1048970, mine("pqrstuv"))
