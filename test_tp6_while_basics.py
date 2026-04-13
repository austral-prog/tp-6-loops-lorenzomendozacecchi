import unittest
import while_basics as ex6


class TP6WhileBasicsCases(unittest.TestCase):

    def test_countdown(self):
        self.assertEqual([5, 4, 3, 2, 1, 0], ex6.countdown(5))
        self.assertEqual([0], ex6.countdown(0))
        self.assertEqual([], ex6.countdown(-1))
        self.assertEqual([3, 2, 1, 0], ex6.countdown(3))
        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], ex6.countdown(10))

    def test_double_until(self):
        self.assertEqual([1, 2, 4, 8], ex6.double_until(10))
        self.assertEqual([1], ex6.double_until(1))
        self.assertEqual([], ex6.double_until(0))
        self.assertEqual([1, 2, 4, 8, 16, 32, 64], ex6.double_until(100))
        self.assertEqual([1, 2, 4, 8, 16], ex6.double_until(16))


if __name__ == '__main__':
    unittest.main()
