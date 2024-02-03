from utils.utils import print_list, create_linked_list


def reverse_linked_list(head):
    if head is None:
        return None
    
    previous_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

values = [1,3,5,7,9]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)

### REVERSED LINKED LIST IN-PLACE ###
my_reverse_linked_list = reverse_linked_list(my_linked_list)
print_list(my_reverse_linked_list)
