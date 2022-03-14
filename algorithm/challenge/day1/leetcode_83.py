class ListNode:

    def __init__(self, x) -> None:
        self.x = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

if __name__ == '__main__':
    node = ListNode(1)
    print(node)