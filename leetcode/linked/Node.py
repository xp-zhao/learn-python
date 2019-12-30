class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        char = '->'
        val_list = []
        while self is not None:
            val_list.append(str(self.val))
            self = self.next
        return char.join(val_list)

    def set_next(self, node_next):
        self.next = node_next

    @staticmethod
    def init_by_list(node_list):
        pre, head = None, None
        for i, v in enumerate(node_list):
            item = Node(v)
            if pre is not None:
                pre.next = item
            else:
                head = item
            pre = item
        return head


if __name__ == '__main__':
    node = Node(1)
    node1 = Node(2)
    node.next = node1
    print(node)
