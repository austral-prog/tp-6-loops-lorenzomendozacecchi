import unittest
import enumerate_list as ex3


class TP6EnumerateListCases(unittest.TestCase):

    def test_enumerate_list(self):
        self.assertEqual(
            ["0. Red", "1. Green", "2. White", "3. Black"],
            ex3.enumerate_list(["Red", "Green", "", "White", "Black"])
        )

    def test_enumerate_list_no_empties(self):
        self.assertEqual(
            ["0. Red", "1. Green", "2. Blue"],
            ex3.enumerate_list(["Red", "Green", "Blue"])
        )

    def test_enumerate_list_all_empty(self):
        self.assertEqual([], ex3.enumerate_list(["", "", ""]))

    def test_enumerate_list_empty_input(self):
        self.assertEqual([], ex3.enumerate_list([]))

    def test_enumerate_backwards(self):
        self.assertEqual(
            ["0. deR", "1. neerG", "2. etihW", "3. kcalB"],
            ex3.enumerate_backwards(["Red", "Green", "", "White", "Black"])
        )

    def test_enumerate_backwards_no_empties(self):
        self.assertEqual(
            ["0. olleH", "1. dlroW"],
            ex3.enumerate_backwards(["Hello", "World"])
        )

    def test_enumerate_backwards_empty_input(self):
        self.assertEqual([], ex3.enumerate_backwards([]))


if __name__ == '__main__':
    unittest.main()
