public class RemoveDuplicate {
    public int removeDuplicates(int[] nums) {
        int result = 1;
        int counter = 1;
        for(int i = 0; i < nums.length - 1; i++){
            if(nums[i] != nums[i+1]){
                result++;
                nums[counter] = nums[i+1];
                counter++;
            }
        }
        return result;
    }
}
