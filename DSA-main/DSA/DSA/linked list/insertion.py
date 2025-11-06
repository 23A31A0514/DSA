class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert_at_position(self, pos, val):
        """Insert value at position pos (0-based).
           If pos <= 0 -> insert at head. If pos >= length -> insert at tail."""
        if pos <= 0 or not self.head:
            self.insert_at_head(val)
            return
        cur = self.head
        index = 0
        while cur.next and index < pos - 1:
            cur = cur.next
            index += 1
        node = Node(val)
        node.next = cur.next
        cur.next = node

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

# Example usage
ll = LinkedList()
ll.insert_at_head(3)        # 3
ll.insert_at_head(2)        # 2 -> 3
ll.insert_at_tail(5)        # 2 -> 3 -> 5
ll.insert_at_position(2, 4) # 2 -> 3 -> 4 -> 5
print(ll.to_list())         # [2, 3, 4, 5]
