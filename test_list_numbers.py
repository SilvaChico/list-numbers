import unittest
import list_numbers
import time


class TestListNumbers(unittest.TestCase):

    def test_list_numbers_str_for_consecutive_numbers(self):
        self.assertEqual(
            list_numbers.list_numbers_str('1 2'),
            '1 2'
        )

    def test_list_numbers_str_for_non_consecutive_numbers_1(self):
        self.assertEqual(
            list_numbers.list_numbers_str('1 3'),
            '1 2 3'
        )

    def test_list_numbers_str_for_non_consecutive_numbers_2(self):
        self.assertEqual(
            list_numbers.list_numbers_str('9 12'),
            '9 10 11 12'
        )

    def test_list_numbers_str_statig_with_white_space(self):
        self.assertEqual(
            list_numbers.list_numbers_str(' 1 3 '),
            '1 2 3'
        )

    def test_list_numbers_str_with_double_white_spaces(self):
        self.assertEqual(
            list_numbers.list_numbers_str('1   3'),
            '1 2 3'
        )

    def test_list_numbers_str_3_arguments(self):
        with self.assertRaises(list_numbers.OddNumberOfArguments):
            list_numbers.list_numbers_str('1 2 3')

    def test_list_numbers_str_1_argument(self):
        with self.assertRaises(list_numbers.OddNumberOfArguments):
            list_numbers.list_numbers_str('16564')

    def test_list_numbers_str_2_intervals(self):
        self.assertEqual(
            list_numbers.list_numbers_str('2 4 5 7'),
            '2 3 4 5 6 7'
        )

    def test_list_numbers_str_2_intervals_intercepting(self):
        self.assertEqual(
            list_numbers.list_numbers_str('2 4 2 7'),
            '2 3 4 5 6 7'
        )

    def test_list_numbers_str_2_not_sorted_intervals_intercepting(self):
        self.assertEqual(
            list_numbers.list_numbers_str('5 7 2 6'),
            '2 3 4 5 6 7'
        )

    def test_list_numbers_str_3_intervals(self):
        self.assertEqual(
            list_numbers.list_numbers_str('5 9 2 3 11 15'),
            '2 3 5 6 7 8 9 11 12 13 14 15'
        )

    def test_list_numbers_str_10_intervals(self):
        self.assertEqual(
            list_numbers.list_numbers_str(
                '5 9 2 3 11 15 100 105 8 9 25 28 99 101 44 49 30 40 1000 1003'
            ),
            '2 3 5 6 7 8 9 11 12 13 14 15 25 26 27 28 30 31 32 33 34 35 36 37 '
            '38 39 40 44 45 46 47 48 49 99 100 101 102 103 104 105 1000 1001 '
            '1002 1003'
        )

    def test_list_numbers_str_interval_in_inverse_order(self):
        self.assertEqual(
            list_numbers.list_numbers_str('3 1'),
            '1 2 3'
        )

    def test_list_numbers_str_empty_string(self):
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('')

    def test_list_numbers_str_negative_value(self):
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('-1 1')

    def test_list_numbers_str_non_digit_character(self):
        with self.assertRaises(list_numbers.InvalidArguments):
            list_numbers.list_numbers_str('1 2 3%')

    def test_list_numbers_str_with_one_million_output(self):

        expected = ' '.join(
            map(str,
                range(0, 1000000+1)
                )
        )

        self.assertEqual(
            list_numbers.list_numbers_str('100 1000000 0 100'),
            expected
        )

    def test_list_numbers_str_10_intervals_with_one_million_output_timed(self):

        time_before_one_interval = time.time()
        list_numbers.list_numbers_str('0 1000000')
        time_after_one_interval = time.time()
        elapsed_seconds_one_interval = time_after_one_interval - time_before_one_interval

        expected = ' '.join(
            map(
                str,
                range(0, 1000000+1)
            )
        )

        time_before_ten_intervals = time.time()
        result = list_numbers.list_numbers_str(
            (
                '0 999991 '
                '1 999992 '
                '2 999993 '
                '3 999994 '
                '4 999995 '
                '5 999996 '
                '6 999997 '
                '7 999998 '
                '8 999999 '
                '9 1000000'
            )
        )
        time_after_ten_intervals = time.time()
        elapsed_seconds_ten_intervals = time_after_ten_intervals - time_before_ten_intervals

        self.assertEqual(result, expected)
        self.assertLess(
            elapsed_seconds_ten_intervals,
            elapsed_seconds_one_interval * 2
        )


if __name__ == '__main__':
    unittest.main()
