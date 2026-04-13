import unittest
import sum_range as ex1


class TP6SumRangeCases(unittest.TestCase):

    def test_sum_to_n(self):
        self.assertEqual(15, ex1.sum_to_n(5))
        self.assertEqual(1, ex1.sum_to_n(1))
        self.assertEqual(0, ex1.sum_to_n(0))
        self.assertEqual(0, ex1.sum_to_n(-3))
        self.assertEqual(5050, ex1.sum_to_n(100))
        self.assertEqual(55, ex1.sum_to_n(10))

    def test_sum_evens(self):
        self.assertEqual(30, ex1.sum_evens(10))
        self.assertEqual(12, ex1.sum_evens(7))
        self.assertEqual(2, ex1.sum_evens(2))
        self.assertEqual(0, ex1.sum_evens(1))
        self.assertEqual(0, ex1.sum_evens(0))
        self.assertEqual(0, ex1.sum_evens(-5))
        self.assertEqual(20, ex1.sum_evens(9))

    def test_factorial(self):
        self.assertEqual(120, ex1.factorial(5))
        self.assertEqual(1, ex1.factorial(1))
        self.assertEqual(1, ex1.factorial(0))
        self.assertEqual(1, ex1.factorial(-2))
        self.assertEqual(720, ex1.factorial(6))
        self.assertEqual(3628800, ex1.factorial(10))


if __name__ == '__main__':
    unittest.main()
