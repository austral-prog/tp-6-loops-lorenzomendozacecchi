import unittest
import search as ex4


class TP6SearchCases(unittest.TestCase):

    def test_index_of_found(self):
        colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        self.assertEqual(3, ex4.index_of("Black", colors))

    def test_index_of_first_element(self):
        colors = ["Red", "Green", "White"]
        self.assertEqual(0, ex4.index_of("Red", colors))

    def test_index_of_not_found(self):
        colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        self.assertEqual(-1, ex4.index_of("Blue", colors))

    def test_index_of_by_index(self):
        colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        self.assertEqual(3, ex4.index_of_by_index("Black", colors, 1))
        self.assertEqual(6, ex4.index_of_by_index("Black", colors, 4))
        self.assertEqual(-1, ex4.index_of_by_index("Green", colors, 2))

    def test_index_of_by_index_at_start(self):
        colors = ["Red", "Green", "White"]
        self.assertEqual(0, ex4.index_of_by_index("Red", colors, 0))

    def test_index_of_empty_found(self):
        colors = ["Red", "Green", "", "", "Pink", "", "Black"]
        self.assertEqual(2, ex4.index_of_empty(colors))

    def test_index_of_empty_not_found(self):
        colors = ["Red", "Green", "White", "Black"]
        self.assertEqual(-1, ex4.index_of_empty(colors))

    def test_index_of_empty_first(self):
        colors = ["", "Red", "Green"]
        self.assertEqual(0, ex4.index_of_empty(colors))


if __name__ == '__main__':
    unittest.main()
