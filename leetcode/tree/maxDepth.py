from leetcode.tree.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        max_depth = max(left_depth, right_depth) + 1
        return max_depth


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    s = Solution()
    print(s.maxDepth(t1))
