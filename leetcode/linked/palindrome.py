from leetcode.linked.Node import Node as ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        while head is not None:
            val_list.append(head.val)
            head = head.next
        length = len(val_list)
        for i in range(length // 2):
            if val_list[i] != val_list[length - 1 - i]:
                return False
        return True

    def slow_fast_pointer(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
            cur.next = pre
            pre = cur
        if fast is not None:
            slow = slow.next
        while pre and slow:
            if pre.val != slow.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
        # print(pre)
        # print(slow)
        # print(fast)


if __name__ == '__main__':
    node = ListNode.init_by_list([1, 2, 3, 4, 5])
    s = Solution()
    # print(s.isPalindrome(node))
    print(s.slow_fast_pointer(node))
