from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        # find
        while fast != slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return fast == slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        # find
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # no cycle
        if not fast or not fast.next:
            return None
        # find node
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow