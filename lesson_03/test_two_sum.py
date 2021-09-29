import unittest
from two_sum import two_sum_primary, two_sum_optimized
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_primary(self):
        self.assertEqual(two_sum_primary([1, 2, 3, 5, 9], 10), [1, 9])

    def test_optimized(self):
        self.assertEqual(two_sum_optimized([1, 2, 3, 5, 9], 8), [3, 5])