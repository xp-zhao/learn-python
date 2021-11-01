# 求两数之和, 双重循环暴力求值时间复杂度太高, 可以使用哈希表减少时间复杂度
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        num_dict = {}
        for index, value in enumerate(nums):
            num_dict[value] = index
        print(num_dict)
        for index, value in enumerate(nums):
            diff = target - value
            if diff in num_dict and index != num_dict[diff]:
                return [index, num_dict[diff]]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1, 2, 3], 6))
