# def how_long(first, *other):
# #     print(1 * len(other))
# #
# #
# # how_long(1)
# #
# # for i in range(10, 20, 2):
# #     print(i)
# #
# #
# # def f_range(start, stop, step):
# #     x = start
# #     while x < stop:
# #         yield x
# #         x += step
#
#
# for i in f_range(10, 20, 0.5):
#     print(i)
#
#
# def add(x, y):
#     return x + y
#
#
# var = lambda x, y: x + y
# print(var(1, 2))
# print(add(1, 2))
#
# a = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 2, a)))
#
# print(list(map(lambda x: x + 1, a)))
#
# b = [1, 2, 3]
# c = [4, 5, 6]
# print(list(map(lambda x, y: x + y, b, c)))

# from functools import reduce
# 
# print(reduce(lambda x, y: x + y, [2, 3, 4], 1))
# 
# for i in zip((1,2,3),(4,5,6)):
#     print(i)


def add(a, b):
    return lambda x: a * x + b


num = add(1, 3)
print(num(2))
