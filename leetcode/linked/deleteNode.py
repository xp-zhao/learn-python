from leetcode.linked.Node import Node


class Solution:
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    node = Node.init_by_list([4, 5, 1, 9])
    print(node)
    head = node
    d_node = None
    while head is not None:
        if head.val == 5:
            d_node = head
            break
        head = head.next
    s = Solution()
    s.delete_node(d_node)
    print(node)
