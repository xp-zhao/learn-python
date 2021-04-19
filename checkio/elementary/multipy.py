def mult_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example: ")
    print(mult_two(2, 3))
    assert mult_two(2, 3) == 6
    assert mult_two(1, 0) == 0
