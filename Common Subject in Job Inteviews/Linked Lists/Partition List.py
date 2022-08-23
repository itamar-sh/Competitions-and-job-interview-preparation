# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = None
        new_mid = None
        small = None
        big = None
        cur = head
        while cur is not None:
            if cur.val < n:
                if small is None:
                    small = cur
                    new_head = cur
                else:
                    small.next = cur
                    small = cur
            if cur.val >= n:
                if big is None:
                    big = cur
                    new_mid = cur
                else:
                    big.next = cur
                    big = cur
            cur = cur.next
        if big is not None:
            big.next = None
        if small is not None:
            small.next = new_mid
            return new_head
        else:  # small is None so everything is big
            return new_mid

