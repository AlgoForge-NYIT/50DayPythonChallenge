### UTILITY FUNCTIONS ###

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current_node = head
    nodes = []
    while current_node is not None and len(nodes) < 10:
        nodes.append(str(current_node.value))
        current_node = current_node.next
    print(" -> ".join(nodes) + "-> ...")

def create_linked_list(values):
    if not values:
        return None

    head = LinkedListNode(values[0])
    current_node = head
    for value in values[1:]:
        next_node = LinkedListNode(value)
        current_node.next = next_node
        current_node = current_node.next
    return head

