# f(n) = f(n - 1) + 1, f(1) = 1
def f(n):
    if n == 1:
        return 1;
    return f(n - 1) + 1


# f(n) = f(n - 1) + f(n - 2)
# f(1) = 1
# f(2) = 2
temp_dict = {1: 1, 2: 2}


def f_1(n):
    if n in temp_dict:
        return temp_dict[n]
    result = f_1(n - 2) + f_1(n - 1)
    temp_dict[n] = result
    print(temp_dict)
    return result


if __name__ == '__main__':
    f_1(10)
