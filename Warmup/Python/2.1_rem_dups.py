
from utils.utils import print_list, create_linked_list, LinkedListNode

def remove_duplicates(head):
    current_node = head
    numbers_seen = set()
    prev_node = None

    while current_node:
        if current_node.value in numbers_seen:
            next_node = current_node.next
            prev_node.next = next_node
            current_node = next_node
        else:
            numbers_seen.add(current_node.value)
            prev_node = current_node
            current_node = current_node.next
    return head

values = [1,3,3,4,4,5,5]
my_linked_list = create_linked_list(values)
print("My linked list with duplicates: ")
print_list(my_linked_list)
print("My linked list without duplicates: ")
my_linked_list_no_dups = remove_duplicates(my_linked_list)
print_list(my_linked_list_no_dups)

### no buffer ###
def remove_duplicates_v2(head):
    runner_one = head

    while runner_one:
        prev_runner_two = runner_one
        runner_two = runner_one.next
        while runner_two:
            if runner_two.value == runner_one.value:
                prev_runner_two.next = runner_two.next
                runner_two = runner_two.next
            else:
                prev_runner_two = runner_two
                runner_two = runner_two.next
        runner_one = runner_one.next
   
    return head


values = [1,3,3,4,4,5,5]
my_linked_list = create_linked_list(values)
print("My linked list with duplicates: ")
print_list(my_linked_list)
print("My linked list without duplicates: ")
my_linked_list_no_dups = remove_duplicates_v2(my_linked_list)
print_list(my_linked_list_no_dups)

