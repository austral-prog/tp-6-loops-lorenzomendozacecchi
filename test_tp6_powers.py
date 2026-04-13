import unittest
import powers as ex2


class TP6PowersCases(unittest.TestCase):

    def test_power(self):
        self.assertEqual(8, ex2.power(2, 3))
        self.assertEqual(1, ex2.power(5, 0))
        self.assertEqual(81, ex2.power(3, 4))
        self.assertEqual(100, ex2.power(10, 2))
        self.assertEqual(1, ex2.power(1, 100))
        self.assertEqual(0, ex2.power(0, 5))
        self.assertEqual(1, ex2.power(0, 0))

    def test_sum_of_powers(self):
        self.assertEqual(15, ex2.sum_of_powers(2, 3))
        self.assertEqual(13, ex2.sum_of_powers(3, 2))
        self.assertEqual(1, ex2.sum_of_powers(5, 0))
        self.assertEqual(31, ex2.sum_of_powers(2, 4))
        self.assertEqual(3, ex2.sum_of_powers(2, 1))
        self.assertEqual(11111, ex2.sum_of_powers(10, 4))


if __name__ == '__main__':
    unittest.main()
