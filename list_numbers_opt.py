def list_numbers(intervals):
    print(list_numbers_str(intervals))


def list_numbers_str(intervals):
    if not intervals.replace(' ', '').isdigit():
        raise InvalidArguments('invalid arguments')

    intervals_list = [*map(int, remove_double_white_spaces(intervals).split())]

    if is_odd(len(intervals_list)):
        raise OddNumberOfArguments('odd number of arguments')

    intervals = zip(intervals_list[0::2],  intervals_list[1::2])

    itervals_union = []
    for a, b in sorted(intervals):
        upper_limit, lower_limit = max(a, b), min(a, b)
        itervals_union = union(itervals_union, [lower_limit, upper_limit])

    return " ".join(map(str, generate_numbers_list(itervals_union)))


def generate_numbers_list(intervals):
    list_of_numbers = []
    for a, b in intervals:
        list_of_numbers += [*range(a, b + 1)]
    return list_of_numbers


def union(lst1, intervals):
    if lst1 and lst1[-1][1] >= intervals[0] - 1:
        lst1[-1][1] = max(lst1[-1][0], intervals[1])
    else:
        lst1.append([intervals[0], intervals[1]])
    return lst1


def remove_double_white_spaces(string):
    return ' '.join(string.split())


def is_odd(number):
    return number % 2 != 0


class OddNumberOfArguments(Exception):
    pass


class InvalidArguments(Exception):
    pass
