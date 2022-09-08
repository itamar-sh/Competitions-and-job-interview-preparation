from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head
        # add node identical for every original node
        old = head
        while old:
            temp = old.next
            new = Node(old.val, temp, old.random)
            old.next = new
            old = temp
        # take every new node and add their random by 1: now they point to new identical random node
        cur = head
        index = 0
        while cur:
            if index % 2 == 1:
                cur.random = cur.random.next
            cur = cur.next
            index += 1
        # seperate the lists
        cur = head
        new_head = head.next
        while cur and cur.next:
            cur.next, cur = cur.next.next, cur.next
        return new_head