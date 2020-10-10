class ListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return '{val}->{next}'.format(val=self.val, next=self.next)


head = ListNode(1)
node1 = ListNode(2)
head.next = node1
print(head)
