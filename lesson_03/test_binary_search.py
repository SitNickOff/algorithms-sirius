import unittest
from binary_search import binary_search


class TestCircleArea(unittest.TestCase):
    def test_primary(self):
        self.assertEqual(binary_search([0,1,7,19,17,20,10],20),5)
