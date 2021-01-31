import unittest
import list_numbers


class TestListNumbers(unittest.TestCase):

    def test_list_numbers_str(self):
        self.assertEqual(list_numbers.list_numbers_str('1 2'), '1 2')
        self.assertEqual(list_numbers.list_numbers_str('1 3'), '1 2 3')
        self.assertEqual(
            list_numbers.list_numbers_str('9 12'), '9 10 11 12')
        self.assertEqual(
            list_numbers.list_numbers_str(' 1 3 '), '1 2 3')
        self.assertEqual(
            list_numbers.list_numbers_str('1   3'), '1 2 3')
        with self.assertRaises(list_numbers.OddNumberOfArguments):
            list_numbers.list_numbers_str('1 2 3')
        self.assertEqual(list_numbers.list_numbers_str('1 2 5 6'), '1 2 5 6')
        self.assertEqual(list_numbers.list_numbers_str(
            '2 4 5 7'), '2 3 4 5 6 7')
        self.assertEqual(list_numbers.list_numbers_str(
            '2 4 2 7'), '2 3 4 5 6 7')
        self.assertEqual(list_numbers.list_numbers_str(
            '5 7 2 4'), '2 3 4 5 6 7')
        self.assertEqual(list_numbers.list_numbers_str(
            '5 9 2 3 11 15'), '2 3 5 6 7 8 9 11 12 13 14 15')
        self.assertEqual(list_numbers.list_numbers_str(
            '5 9 2 3 11 15 100 105 8 9 25 28 99 101 44 49 30 40 1000 1003'), '2 3 5 6 7 8 9 11 12 13 14 15 25 26 27 28 30 31 32 33 34 35 36 37 38 39 40 44 45 46 47 48 49 99 100 101 102 103 104 105 1000 1001 1002 1003')
        self.assertEqual(list_numbers.list_numbers_str('3 1'), '1 2 3')
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('')
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('-1 1')
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('1 2 3%')


if __name__ == '__main__':
    unittest.main()
