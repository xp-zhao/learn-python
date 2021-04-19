def nearest_value(values: set, one: int) -> int:
    # your code here
    # if one in values:
    #     return one
    # min_dict = {}
    # min_distance = abs(list(values)[0] - one)
    # for value in values:
    #     distance = abs(value - one)
    #     if str(distance) in min_dict:
    #         min_dict[str(distance)] = min(value, min_dict[str(distance)])
    #     else:
    #         min_dict[str(distance)] = value
    #     if distance < min_distance:
    #         min_distance = distance
    # return min_dict[str(min_distance)]
    if one in values:
        return one
    min_distance = min([abs(value - one) for value in values])
    return min([value for value in values if abs(value - one) == min_distance])


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
