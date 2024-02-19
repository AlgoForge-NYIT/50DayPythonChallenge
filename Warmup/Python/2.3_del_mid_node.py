from utils.utils import print_list, create_linked_list, LinkedListNode
from utils.del_node import length


def find_middle_node(LL, k):
    current_node = LL
    length_LL = length(LL)
    if length_LL < 3 and k < 2:
        return None
    
    for i in range(k - 1):
        current_node = current_node.next
    
    return current_node



def delete_mid_node(mid_node):    
    next_next_node = mid_node.next.next
    mid_node.value = mid_node.next.value
    mid_node.next = next_next_node 


values = [1,2,3]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)

print("Find middle node with k = 2, where k is the middle node")
middle_node = find_middle_node(my_linked_list, 2)
print("middle node value: ", middle_node.value)
print("Now deleting this middle node...")
delete_mid_node(middle_node)
print_list(my_linked_list)

