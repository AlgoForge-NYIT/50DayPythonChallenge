# This helper function calculates the length of a linked list
def length(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count
