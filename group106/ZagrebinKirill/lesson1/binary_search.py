import unittest
from time import time


def binary_search(array, num):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + high
        guess = array[mid]

        if guess == num:
            return mid
        if guess > mid:
            high = mid - 1
        if guess < mid:
            low = mid + 1

    return -1


class BinarySearchTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), 3)
        self.assertEqual(binary_search([2, 3, 4, 5, 6, 7, 8, 9, 10], 1), -1)
