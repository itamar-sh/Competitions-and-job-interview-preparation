from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        remainder = 0
        while l1 and l2:
            value = l1.val + l2.val + remainder
            cur.next = ListNode(value % 10)
            remainder = value // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 else l2
        while l:
            value = l.val + remainder
            cur.next = ListNode(value % 10)
            remainder = value // 10
            cur = cur.next
            l = l.next
        if remainder:
            cur.next = ListNode(remainder)
            cur = cur.next
        return head.next