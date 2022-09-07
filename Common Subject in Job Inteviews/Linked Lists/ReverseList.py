from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        next_node = head.next
        head.next = None
        while next_node:
            temp = next_node.next
            next_node.next = cur
            cur = next_node
            next_node = temp
        return cur