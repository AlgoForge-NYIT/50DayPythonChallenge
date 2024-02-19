public class RemoveElem {
    public int removeElement(int[] nums, int val) {
        int result = 0;
        int counter = 0;
        for(int i = 0; i < nums.length; i++){
            // if the val does not equal to the number in array:
            if(nums[i] != val){
                nums[counter] = nums[i];
                counter++;
                result++;
            }
        }

        return result;
    }
}
