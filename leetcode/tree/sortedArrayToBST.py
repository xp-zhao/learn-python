from leetcode.tree.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    root = s.sortedArrayToBST(nums)
    print(root)
