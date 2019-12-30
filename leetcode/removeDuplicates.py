from leetcode.linked.Node import Node


def remove(node):
    cur = node
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next


linked = Node.init_by_list([1, 1, 2, 3, 3])
remove(linked)
print(linked)
