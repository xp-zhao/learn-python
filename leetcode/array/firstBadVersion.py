class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            if self.isBadVersion(mid):
                start = mid + 1
            elif not self.isBadVersion(mid - 1):
                end = mid - 1
            else:
                return mid
        return None

    def isBadVersion(self, version):
        pass

    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return None


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    target = 6
    s = Solution()
    print(s.binarySearch(nums, target))
