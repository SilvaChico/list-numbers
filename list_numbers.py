def list_numbers(intervals):
    print(list_numbers_str(intervals))


def list_numbers_str(intervals):
    if not intervals.replace(" ", "").isdigit():
        raise InvalidArguments('invalid arguments')

    interval_list = remove_double_white_spaces(intervals).split()

    if is_odd(len(interval_list)):
        raise OddNumberOfAguments('odd number of arguments')

    all_numbers = []
    for i in range(0, len(interval_list), 2):
        upper_limit = max(int(interval_list[i]), int(interval_list[i+1]))
        lower_limit = min(int(interval_list[i]), int(interval_list[i+1]))
        all_numbers += [*range(lower_limit, upper_limit+1)]

    sorted_unique_numbers = sorted(remove_duplicates(all_numbers))

    return " ".join(map(str, sorted_unique_numbers))


def remove_duplicates(list):
    res = []
    [res.append(x) for x in list if x not in res]
    return res


def remove_double_white_spaces(string):
    return ' '.join(string.split())


def is_odd(number):
    return number % 2 != 0


class OddNumberOfAguments(Exception):
    pass


class InvalidArguments(Exception):
    pass
