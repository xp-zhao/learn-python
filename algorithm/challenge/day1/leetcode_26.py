from pip import main


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
    
if __name__ == '__main__':
    s = Solution()
    assert s.removeDuplicates([1, 1, 2]) == 2
    assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
