class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sub = nums[0]
        sum_num = 0
        for i in nums:
            if sum_num < 0:
                sum_num = i
            else:
                sum_num += i
            max_sub = max(max_sub, sum_num)
        return max_sub

    def maxSub(self, nums):
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    nums_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums_list))
    print(s.maxSub(nums_list))
