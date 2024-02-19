public class SearchInsert {
    public int searchInsert(int[] nums, int target) {
        int result = 0;
        for(int i = 0; i < nums.length; i++){
            if(i == nums.length - 1 && nums[i] < target){
                result = i+1;
            }
            if(nums[i] == target || nums[i] > target){
                result = i;
                break;
            }
        }
        return result;
    }
}
