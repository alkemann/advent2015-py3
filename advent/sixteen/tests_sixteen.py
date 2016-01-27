from unittest import TestCase
from sixteen import *


class TestSixsteen(TestCase):
    def test_sue(self):
        sue = Sue("Sue 460: vizslas: 4, cats: 6, perfumes: 2")

        self.assertEqual(460, sue.id)
        self.assertEqual(4, sue.hints["vizslas"])
