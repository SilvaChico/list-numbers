def list_numbers(intervals):
    print(list_numbers_str(intervals))


def list_numbers_str(intervals):
    if not intervals.replace(' ', '').isdigit():
        raise InvalidArguments('invalid arguments')

    intervals_list = [*map(int, remove_double_white_spaces(intervals).split())]

    if is_odd(len(intervals_list)):
        raise OddNumberOfArguments('odd number of arguments')

    intervals = zip(intervals_list[0::2], intervals_list[1::2])

    list_of_numbers = []
    for a, b in intervals:
        upper_limit, lower_limit = max(a, b), min(a, b)
        list_of_numbers = union(
            list_of_numbers, [*range(lower_limit, upper_limit+1)])

    sorted_numbers = sorted(list_of_numbers)

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
