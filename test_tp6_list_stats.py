import unittest
import list_stats as ex10


class TP6ListStatsCases(unittest.TestCase):

    def test_range_of(self):
        self.assertEqual(6, ex10.range_of([3, 1, 7, 2]))
        self.assertEqual(0, ex10.range_of([5, 5, 5]))
        self.assertEqual(9, ex10.range_of([1, 10]))
        self.assertEqual(15, ex10.range_of([-5, 10, 3]))

    def test_average(self):
        self.assertEqual(20.0, ex10.average([10, 20, 30]))
        self.assertEqual(0.0, ex10.average([]))
        self.assertEqual(5.0, ex10.average([5]))
        self.assertEqual(2.5, ex10.average([1, 2, 3, 4]))
        self.assertEqual(3.3, ex10.average([1, 2, 7]))

    def test_describe(self):
        self.assertEqual(
            "Min:1 Max:7 Range:6 Avg:3.2",
            ex10.describe([3, 1, 7, 2])
        )

    def test_describe_single(self):
        self.assertEqual(
            "Min:5 Max:5 Range:0 Avg:5.0",
            ex10.describe([5])
        )

    def test_describe_negative(self):
        self.assertEqual(
            "Min:-5 Max:10 Range:15 Avg:2.7",
            ex10.describe([-5, 10, 3])
        )

    def test_describe_empty(self):
        self.assertEqual("Empty list", ex10.describe([]))


if __name__ == '__main__':
    unittest.main()
