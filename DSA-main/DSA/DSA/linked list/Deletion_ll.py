class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, position):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head

        # Case 1: delete first node
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next
        
        # Node to delete
        node_to_delete = temp.next
        temp.next = node_to_delete.next
        node_to_delete = None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Before Deletion:")
ll.display()

ll.delete(2)  
print("After Deletion:")
ll.display()
