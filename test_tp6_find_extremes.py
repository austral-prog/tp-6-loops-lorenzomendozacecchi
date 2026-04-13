import unittest
import find_extremes as ex9


class TP6FindExtremesCases(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(1, ex9.find_min([3, 1, 7, 2]))
        self.assertEqual(5, ex9.find_min([5, 5, 5]))
        self.assertEqual(-7, ex9.find_min([-3, -1, -7]))
        self.assertEqual(1, ex9.find_min([1]))
        self.assertEqual(-5, ex9.find_min([-5, 10, 3]))
        self.assertEqual(1, ex9.find_min([1, 2, 3, 4, 5]))

    def test_find_max(self):
        self.assertEqual(7, ex9.find_max([3, 1, 7, 2]))
        self.assertEqual(5, ex9.find_max([5, 5, 5]))
        self.assertEqual(-1, ex9.find_max([-3, -1, -7]))
        self.assertEqual(1, ex9.find_max([1]))
        self.assertEqual(10, ex9.find_max([-5, 10, 3]))
        self.assertEqual(5, ex9.find_max([5, 4, 3, 2, 1]))

    def test_count_negatives(self):
        self.assertEqual(2, ex9.count_negatives([3, -1, -7, 2]))
        self.assertEqual(0, ex9.count_negatives([1, 2, 3]))
        self.assertEqual(3, ex9.count_negatives([-1, -2, -3]))
        self.assertEqual(0, ex9.count_negatives([]))
        self.assertEqual(0, ex9.count_negatives([0, 1, 2]))
        self.assertEqual(1, ex9.count_negatives([-5, 10, 3]))


if __name__ == '__main__':
    unittest.main()
