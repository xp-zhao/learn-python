from leetcode.tree.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        result = []
        self.add_list(root, 0, result)
        return result

    def add_list(self, root, level, result):
        if root is None:
            return
        if len(result) - 1 < level:
            result.append([])
        result[level].append(root.val)
        self.add_list(root.left, level + 1, result)
        self.add_list(root.right, level + 1, result)


if __name__ == "__main__":
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
    print(s.levelOrder(t1))
