import unittest


def two_sum(array, num):
    for i in array:
        if (num - i) in array:
            return [i, num - i]
    return -1


class TwoSumOptimizeTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(two_sum([1, 2, 3, 5, 7, 9], 9), [2, 7])
        self.assertEqual(two_sum([1, 2, 3, 5, 7, 9], 8), [1, 7])
        self.assertEqual(two_sum([1, 2, 3, 5, 7, 9], 10), [1, 9])
        self.assertEqual(two_sum([1, 2, 3, 5, 7, 9], 14), [5, 9])
