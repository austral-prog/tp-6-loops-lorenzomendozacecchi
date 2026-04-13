import unittest
import collatz as ex7


class TP6CollatzCases(unittest.TestCase):

    def test_collatz_steps(self):
        self.assertEqual(0, ex7.collatz_steps(1))
        self.assertEqual(1, ex7.collatz_steps(2))
        self.assertEqual(8, ex7.collatz_steps(6))
        self.assertEqual(6, ex7.collatz_steps(10))
        self.assertEqual(111, ex7.collatz_steps(27))

    def test_collatz_sequence(self):
        self.assertEqual([1], ex7.collatz_sequence(1))
        self.assertEqual([2, 1], ex7.collatz_sequence(2))
        self.assertEqual(
            [6, 3, 10, 5, 16, 8, 4, 2, 1],
            ex7.collatz_sequence(6)
        )
        self.assertEqual(
            [10, 5, 16, 8, 4, 2, 1],
            ex7.collatz_sequence(10)
        )

    def test_collatz_sequence_ends_at_one(self):
        seq = ex7.collatz_sequence(27)
        self.assertEqual(27, seq[0])
        self.assertEqual(1, seq[-1])
        self.assertEqual(112, len(seq))


if __name__ == '__main__':
    unittest.main()
