import sys


def list_numbers(intervals):
    print(list_numbers_str(intervals))


def list_numbers_str(intervals):
    if not intervals.replace(' ', '').isdigit():
        raise InvalidArguments('invalid arguments')

    intervals_list = remove_double_white_spaces(intervals).split()
    if is_odd(len(intervals_list)):
        raise OddNumberOfArguments('odd number of arguments')

    intervals_numbers = [*map(int, intervals_list)]
    interval_pairs = zip(intervals_numbers[0::2], intervals_numbers[1::2])

    numbers = []
    for a, b in interval_pairs:
        upper_limit, lower_limit = max(a, b), min(a, b)
        numbers = union(
            numbers, [*range(lower_limit, upper_limit+1)]
        )

    sorted_numbers = sorted(numbers)

    return " ".join(map(str, sorted_numbers))


def union(lst1, lst2):
    return list(set(lst1) | set(lst2))


def remove_double_white_spaces(string):
    return ' '.join(string.split())


def is_odd(number):
    return number % 2 != 0


class OddNumberOfArguments(Exception):
    pass


class InvalidArguments(Exception):
    pass


if __name__ == '__main__':
    list_numbers(sys.argv[1])
