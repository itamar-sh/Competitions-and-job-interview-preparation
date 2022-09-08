from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
    and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself
    """
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

    """
    You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes 
    first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itsel
    """
    def addTwoNumbers2(self, l1, l2):
        s1 = 0
        s2 = 0
        while l1:
            s1 *= 10
            s1 += l1.val
            l1 = l1.next
        while l2:
            s2 *= 10
            s2 += l2.val
            l2 = l2.next

        s3 = s1 + s2
        tail = None
        head = None
        while s3 > 0:
            head = ListNode(s3 % 10)
            head.next = tail
            tail = head
            s3 = s3 // 10
        return head if head else ListNode(0)
