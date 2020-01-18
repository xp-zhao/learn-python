class Solution:
    def rob(self, nums: list) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        return max(self.rob(nums[:-1]), self.rob(nums[:-2]) + nums[length - 1])

    def robDp(self, nums, dp):
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        if dp[length] is None:
            dp[length] = max(self.robDp(nums[:-1], dp),
                             self.robDp(nums[:-2], dp) + nums[length - 1])
        return dp[length]

    def robLoop(self, nums):
        a, b = 0, 0
        for num in nums:
            a, b = max(a, b + num), a
        return a


if __name__ == '__main__':
    num_list = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100,
                249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81, 185, 165,
                217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
    s = Solution()
    dp = [None] * (len(num_list) + 1)
    # print(s.rob(num_list))
    print(s.robLoop(num_list))
    print(s.robDp(num_list, dp))
