class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == "__main__":
    s = Solution()
    list1 = [1, 2, 3, 0, 0, 0]
    len1 = 3
    list2 = [2, 5, 6]
    len2 = 3
    s.merge(list1, len1, list2, len2)
    print(list1)
