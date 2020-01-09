from leetcode.tree.TreeNode import TreeNode


class Solution:
    pre = None

    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            if not self.isValidBST(root.left):
                return False
            if self.pre and root.val <= self.pre.val:
                return False
            self.pre = root
            return self.isValidBST(root.right)
        return True

    def valid(self, root: TreeNode) -> bool:
        self.prev = None

        def isBST(node):
            if node:
                if not isBST(node.left):
                    return False
                if self.prev and node.val <= self.prev.val:
                    return False
                self.prev = node
                return isBST(node.right)
            return True

        return isBST(root)


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(4)
    t3 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    s = Solution()
    print(s.isValidBST(t1))
    print(s.valid(t1))
