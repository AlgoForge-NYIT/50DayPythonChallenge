from utils.utils import print_list, create_linked_list

def kth_to_last_node(head, k):
    slow_runner = head
    fast_runner = head

    for i in range(k - 1):
        fast_runner = fast_runner.next
    
    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next
    
    return slow_runner.value

values = [1,2,3,5,9]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
kth_value = kth_to_last_node(my_linked_list, 2)
print('kth to last node where k = 2 is: ' , kth_value)
