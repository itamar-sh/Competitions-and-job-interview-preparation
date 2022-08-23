class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Remove_Duplicates_From_an_Unsorted_Linked_List_1836(head: Node):
    cur = head
    last = head
    data_set = set()
    while cur is not None:
        if cur.data not in data_set:
            data_set.add(cur.data)
            temp = cur
            cur = cur.next
            last = temp
        else:
            cur = cur.next
            last.next = cur
    return head

# Function to print nodes in a
# given linked lst
def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Driver code
head = Node(10)
head.next = Node(12)
head.next.next = Node(11)
head.next.next.next = Node(11)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(11)
head.next.next.next.next.next.next = Node(10)

print("Linked List before removing duplicates :")
printList(head)
Remove_Duplicates_From_an_Unsorted_Linked_List_1836(head)
print()
print("Linked List after removing duplicates :")
printList(head)

