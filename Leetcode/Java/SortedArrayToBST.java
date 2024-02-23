public class SortedArrayToBST {
    public TreeNode sortedArrayToBST(int[] nums) {
        return insert(nums,0,nums.length-1);
    }
    public TreeNode insert(int[] nums, int low, int high){
        // if the low index is greater than the mid, no more integer
        // stop the recursion
        if(low > high) return null;
        // else:
        // 1. calculate the midpoint
        int mid = (low + high) / 2;
        // 2. create a new node with the midpoint
        TreeNode node = new TreeNode(nums[mid]);
        // 3. recall the function and do the same with left and right
        // so each node is a midpoint
        node.left = insert(nums,low,mid-1);
        node.right = insert(nums,mid+1,high);
        return node;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){}
    TreeNode(int val){this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
