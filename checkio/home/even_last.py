def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) > 0:
        last = array[-1]
        even_list = [num for num in array[::2]]
        return sum(even_list) * last
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
