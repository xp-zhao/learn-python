from leetcode.linked.Node import Node as ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    # node3.next = node1
    s = Solution()
    print(s.hasCycle(node1))

