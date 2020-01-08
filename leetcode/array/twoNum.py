nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    d = {}
    for i, v in enumerate(nums):
        n = target - v
        if n in d:
            return i, d.get(n)
        d[v] = i
    return []


print(two_sum(nums, target))
