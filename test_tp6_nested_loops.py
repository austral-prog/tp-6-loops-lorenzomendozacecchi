import unittest
import nested_loops as ex8


class TP6NestedLoopsCases(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            ex8.flatten([[1, 2], [3, 4], [5, 6]])
        )

    def test_flatten_single_row(self):
        self.assertEqual([1, 2, 3], ex8.flatten([[1, 2, 3]]))

    def test_flatten_empty(self):
        self.assertEqual([], ex8.flatten([]))

    def test_flatten_mixed_sizes(self):
        self.assertEqual(
            [1, 2, 3, 4, 5],
            ex8.flatten([[1], [2, 3], [4, 5]])
        )

    def test_row_sums(self):
        self.assertEqual(
            [6, 15],
            ex8.row_sums([[1, 2, 3], [4, 5, 6]])
        )

    def test_row_sums_single(self):
        self.assertEqual([10], ex8.row_sums([[10]]))

    def test_row_sums_3x3(self):
        self.assertEqual(
            [6, 15, 24],
            ex8.row_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        )

    def test_col_sums(self):
        self.assertEqual(
            [5, 7, 9],
            ex8.col_sums([[1, 2, 3], [4, 5, 6]])
        )

    def test_col_sums_3x3(self):
        self.assertEqual(
            [12, 15, 18],
            ex8.col_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        )

    def test_col_sums_single_row(self):
        self.assertEqual([1, 2, 3], ex8.col_sums([[1, 2, 3]]))


if __name__ == '__main__':
    unittest.main()
