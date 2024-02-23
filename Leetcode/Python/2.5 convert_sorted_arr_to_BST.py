class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
       
def convertArrayToBST(nums, low=None, high=None):
    if low is None or high is None: # use default parameters to set up initial indices
        low = 0
        high = len(nums) - 1

    if low > high: # base case
        return None

    mid = (low + high) // 2
    node = TreeNode(nums[mid]) # root value set with value at mid index
    node.left = convertArrayToBST(nums, low, mid - 1) # left tree construction recursive call
    node.right = convertArrayToBST(nums, mid + 1, high) # right tree construction recursive call

    return node # return root

# process each level of the tree
# process nodes in a queues shifting them one at a time in each loop through each level and add value to result
def print_tree_with_null(node):
    result = [] # output array/list
    queue = [node] # processing queue with root for processing
   
    while queue:
        current = queue.pop(0)  # create pointer to node to traverse tree setting to shifted first element (FIFO)
        if current is None: # check processing queue to add to result
            result.append(None)
        else:
            result.append(current.val) # process node
            queue.append(current.left) # add left and right sub tree for processing
            queue.append(current.right)
       
    for i in range(len(result) - 1, -1, -1): # loop from back and remove trailing Nones
        if result[-1] == None:
            result.pop()
        else:
            return result   