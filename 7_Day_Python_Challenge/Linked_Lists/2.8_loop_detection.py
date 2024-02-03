from utils.utils import print_list
from utils.loop_detection import create_linked_list

def loop_detection(head):
    slow_runner = head
    fast_runner = head

    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner == fast_runner:
            break

    if fast_runner.next is None:
        return "No cycle detected. End of linked list reached!"

    # find beginning of cycle
    slow_runner = head
    while slow_runner != fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next
    return slow_runner.value

### TEST CASES ###

# Loop starts back at "C"
values = ["A", "B", "C", "D", "E", "C"]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
loop_starting_point = loop_detection(my_linked_list)
print(loop_starting_point)  # Expected Output: "C"

# No loop in this list
values = ["A", "B", "C", "D", "E"]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
loop_starting_point = loop_detection(my_linked_list)
print(loop_starting_point)  # Expected Output: "No loop detected"

# Loop starts back at "A"
values = ["A", "A"]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
loop_starting_point = loop_detection(my_linked_list)
print(loop_starting_point)  # Expected Output: "A"

# Loop starts back at "D"
values = ["A", "B", "C", "D", "E", "F", "G", "H", "D"]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
loop_starting_point = loop_detection(my_linked_list)
print(loop_starting_point)  # Expected Output: "D"

# Loop starts back at "E"
values = ["A", "B", "C", "D", "E", "E"]
my_linked_list = create_linked_list(values)
print_list(my_linked_list)
loop_starting_point = loop_detection(my_linked_list)
print(loop_starting_point)  # Expected Output: "E"
