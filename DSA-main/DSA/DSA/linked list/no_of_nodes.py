def count_nodes(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count
