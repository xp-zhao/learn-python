from leetcode.linked.Node import Node


def reverse(node):
    pre = None
    while node is not None:
        current = node
        node = node.next
        current.next = pre
        pre = current
    return pre


node1 = Node(1)
node2 = Node(2)
node1.set_next(node2)
node3 = Node(3)
node2.set_next(node3)

print(node1)
r = reverse(node1)
print(r)
