# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # Pointer to the next node

def traverse(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")   # Marks end of the list


head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

print("Linked List Traversal:")
traverse(head)
