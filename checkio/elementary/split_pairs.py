def split_pairs(a):
    # your code here
    # str_list = []
    # for i in range(0, len(a)):
    #     if i % 2 == 0:
    #         str_list.append(a[i:i + 2])
    # if len(str_list) >= 1 and len(str_list[-1]) == 1:
    #     str_list[-1] = str_list[-1] + '_'
    # return str_list
    if len(a) >= 1 and len(a) % 2 != 0:
        a = a + '_'
    b = [a[i:i + 2] for i in range(0, len(a), 2)]
    return b


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
