class Solution:

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 2, 0, 3]
    s.moveZeroes(nums)
    print(nums)
