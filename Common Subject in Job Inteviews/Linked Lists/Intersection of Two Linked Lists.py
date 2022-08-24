class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def intersection_of_two_linked_lists(self, headA: Node, headB: Node):
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

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
    # Driver code
    head = Node(4)
    head.next = Node(1)
    a = Node(8)
    a.next = Node(4)
    a.next.next = Node(5)
    head.next.next = a
    head2 = Node(5)
    head2.next = Node(6)
    head2.next.next = Node(1)
    head2.next.next.next = a

    assert(a == solver.intersection_of_two_linked_lists(head, head2))

    head = Node(2)
    head.next = Node(6)
    head.next.next = Node(4)
    head2 = Node(1)
    head2.next = Node(5)

    assert (None == solver.intersection_of_two_linked_lists(head, head2))

