from leetcode.linked.Node import Node


class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        node = Node()
        head = node
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 is None:
            node.next = l2
        else:
            node.next = l1
        return head.next


if __name__ == '__main__':
    node1 = Node.init_by_list([1, 2, 4])
    node2 = Node.init_by_list([1, 3, 4])
    s = Solution()
    print(s.mergeTwoLists(node1, node2))
