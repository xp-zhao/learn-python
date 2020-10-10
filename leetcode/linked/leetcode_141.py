class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return "{val}->{next}".format(val=self.val, next=self.next)


def hasCycle(head: ListNode) -> bool:
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


if __name__ == '__main__':
    head_node = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    head_node.next = node1
    node1.next = node2
    node2.next = head_node
    # print(head_node)
    print(hasCycle(head_node))
