import unittest
from linear_search import linear_search


class TestCircleArea(unittest.TestCase):
    def test_primary(self):
        self.assertEqual(linear_search([0,1,7,19,17,20,10],20),5)
        