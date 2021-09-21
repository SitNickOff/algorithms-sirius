import unittest
from Optimizd_Simple import Optimizd


class TestCircleArea(unittest.TestCase):
    def test_primary(self):
        self.assertEqual(Optimizd((6), "-1"))
