from functools import reduce


def f(n):
    return n * n


def fn(x, y):
    return x * 10 + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def f_n(x, y):
        return x * 10 + y

    def char2num(s1):
        return DIGITS[s1]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def ff(n):
    return n is not None


print(list(map(f, [1, 2, 3, 4, 5, 6])))
print(reduce(fn, [1, 2, 3, 4, 5, 6]))
print(str2int('23'))
print(list(filter(lambda x: x is not None, [1, 2, 3, None, 0, 1])))
print(sorted([1, 0, 3, 2, 5, 4, 6], key=lambda x: x + 1, reverse=True))
