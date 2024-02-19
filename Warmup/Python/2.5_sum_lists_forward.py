from utils.sum_lists import length, pad_list, append_to_start
from utils.utils import print_list, create_linked_list, LinkedListNode

def sum_lists(LL1, LL2):
    if not LL1 and not LL2:
        return None
    
    length1 = length(LL1)
    length2 = length(LL2)

    if length1 < length2:
        length1 = pad_list(LL1, length2 - length1)
    elif length1 > length2:
        length2 = pad_list(LL2, length1 - length2)

    head = sum_and_append_lists(LL1, LL2)

    return head

def sum_and_append_lists(List1, List2):
    current_node_one = List1
    current_node_two = List2
 
    stack_one = []
    while current_node_one:
        stack_one.append(current_node_one.value)
        current_node_one = current_node_one.next
    
    stack_two = []
    while current_node_two:
        stack_two.append(current_node_two.value)
        current_node_two = current_node_two.next

    result = None
    carry = 0

    while stack_one or stack_two:
        result_node_one_value = stack_one.pop() if stack_one else 0
        result_node_two_value = stack_two.pop() if stack_two else 0
        
        total = result_node_one_value + result_node_two_value + carry
        carry = total // 10
        new_node = LinkedListNode(total % 10)
        new_node.next = result
        result = new_node

    if carry > 0:
        new_node = LinkedListNode(carry)
        new_node.next = result
        result = new_node

    return result

list_one = [6, 1, 7]
linked_list_one = create_linked_list(list_one)
print_list(linked_list_one)

list_two = [2, 9, 5]
linked_list_two = create_linked_list(list_two)
print_list(linked_list_two)

result_linked_list = sum_lists(linked_list_one, linked_list_two)
print_list(result_linked_list)
