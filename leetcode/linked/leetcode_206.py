class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return "{val}->{next}".format(val=self.val, next=self.next)


def reverse(head_node):
    pre_node = None
    while head_node is not None:
        next_node = head_node.next
        head_node.next = pre_node
        pre_node = head_node
        head_node = next_node
    return pre_node


head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
head.next = node1
node1.next = node2
print(head)
print(reverse(head))
