from leetcode.linked.Node import Node


class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        cur = head
        result = head
        count = 0
        while head is not None:
            count += 1
            head = head.next
        if count == n:
            return cur.next
        while cur is not None:
            count = count - 1
            if count == n:
                cur.next = cur.next.next
                return result
            cur = cur.next
        return None


if __name__ == "__main__":
    n = 2
    node = Node.init_by_list([1, 2, 3, 4, 5])
    s = Solution()
    print(s.removeNthFromEnd(node, n))
