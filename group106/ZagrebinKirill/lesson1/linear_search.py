import unittest


def linear_search(array, number):
    for i in range(0, len(array)):
        if array[i] == number:
            return i
    return -1


class BinarySearchTest(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), 3)
        self.assertEqual(linear_search([2, 3, 4, 5, 6, 7, 8, 9, 10], 1), -1)
