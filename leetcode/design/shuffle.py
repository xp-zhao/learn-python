import random


class Solution:

    def __init__(self, nums: list):
        self.nums = nums

    def reset(self) -> list:
        return self.nums

    def shuffle(self) -> list:
        res = []
        copy_list = self.nums.copy()
        while len(copy_list) > 0:
            index = random.randint(0, len(copy_list) - 1)
            random.shuffle
            res.append(copy_list.pop(index))
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution(nums)
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())
