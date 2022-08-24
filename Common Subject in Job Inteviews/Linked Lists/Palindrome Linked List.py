class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def Palindrome_Linked_List(self, head):
        if not head or not head.next:
            return True
        end1, head2 = self._reverse_half_list(head)
        p1 = head
        p2 = head2
        while p1 and p2:
            if p1.val != p2.val:
                p2 = self._reverse_list(p2)
                end1.next = p2
                return False
            p1 = p1.next
            p2 = p2.next
        head2 = self._reverse_list(head2)
        end1.next = head2
        return True

    def _reverse_half_list(self, head):
        slow = head
        fast = head
        prev = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return prev, self._reverse_list(slow)

    def _reverse_list(self, head):
        head2 = None
        while head:
            temp = head
            head = head.next
            temp.next = head2
            head2 = temp
        return head2

# Function to print nodes in a
# given linked lst
def printList(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()

if __name__ == '__main__':
    solver = Solution()
    head = Node(2)
    head.next = Node(6)
    head.next.next = Node(2)
    assert(solver.Palindrome_Linked_List(head))
    printList(head)
    head = Node(2)
    head.next = Node(6)
    head.next.next = Node(6)
    head.next.next.next = Node(2)
    assert (solver.Palindrome_Linked_List(head))
    printList(head)
    head = Node(2)
    head.next = Node(6)
    head.next.next = Node(3)
    assert (not solver.Palindrome_Linked_List(head))
    printList(head)
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    assert (not solver.Palindrome_Linked_List(head))
    printList(head)
    head = Node(1)
    head.next = Node(2)
    assert (not solver.Palindrome_Linked_List(head))
    printList(head)