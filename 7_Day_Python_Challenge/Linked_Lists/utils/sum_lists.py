### SUM LISTS UTILITY FUNCTIONS ###

# This helper function calculates the length of a linked list
def length(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count

# This helper function pads a linked list with zeros at the start
def pad_list(short_list, padding):
    head = short_list
    for _ in range(padding):
        new_node = LinkedListNode(0)
        new_node.next = head
        head = new_node
    return head

# This helper funciton appends a node at the start of a linked list
def append_to_start(head, node):
    node.next = head
    return node