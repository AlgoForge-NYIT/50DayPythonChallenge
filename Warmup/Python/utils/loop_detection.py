
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    if not values:
        return None

    head = LinkedListNode(values[0])
    current_node = head
    nodes = {values[0]: head}  # Keep track of nodes by their values

    for value in values[1:]:
        if value in nodes:  # Loop start point
            current_node.next = nodes[value]  # Point to existing node to create a loop
            return head

        # Create new node if no loop
        next_node = LinkedListNode(value)
        current_node.next = next_node
        current_node = next_node
        nodes[value] = current_node  # Store this node in case it's a future loop start

    return head