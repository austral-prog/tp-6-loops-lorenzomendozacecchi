import unittest
import list_modify as ex5


class TP6ListModifyCases(unittest.TestCase):

    def test_put_found_empty(self):
        colors = ["Red", "Green", "", "", "Pink", "", "Black"]
        result = ex5.put("Blue", colors)
        self.assertEqual(2, result)
        self.assertEqual("Blue", colors[2])

    def test_put_no_empty(self):
        colors = ["Red", "Green", "White", "Black"]
        result = ex5.put("Blue", colors)
        self.assertEqual(-1, result)

    def test_put_first_slot(self):
        colors = ["", "Red", "Green"]
        result = ex5.put("Blue", colors)
        self.assertEqual(0, result)
        self.assertEqual("Blue", colors[0])

    def test_remove_multiple(self):
        colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result = ex5.remove("Black", colors)
        self.assertEqual(2, result)
        self.assertEqual("", colors[3])
        self.assertEqual("", colors[6])

    def test_remove_not_found(self):
        colors = ["Red", "Green", "White"]
        result = ex5.remove("Blue", colors)
        self.assertEqual(0, result)

    def test_remove_single(self):
        colors = ["Red", "Green", "White"]
        result = ex5.remove("Green", colors)
        self.assertEqual(1, result)
        self.assertEqual(["Red", "", "White"], colors)


if __name__ == '__main__':
    unittest.main()
