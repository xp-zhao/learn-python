from leetcode.tree.TreeNode import TreeNode


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.judge(root.left, root.right)

    def judge(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.judge(left.left, right.right) and self.judge(left.right,
                                                                 right.left)

    def judge_mod(self, left, right):
        if left is None and right is None:
            return True
        if left and right:
            if left.val == right.val:
                return self.judge(left.left, right.right) and self.judge(
                    left.right, right.left)
        return False


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(5)
    t3 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    s = Solution()
    print(s.isSymmetric(t1))
