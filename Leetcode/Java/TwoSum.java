public class TwoSum {

    class Solution {
        public int[] twoSum(int[] nums, int target) {
            int init = 0;
            int[] result = new int[2];
            while(true){
                // stop if the init position reaches to the end:
                if(init == nums.length - 1){
                    break;
                }
                // add and compare:
                for(int i = init+1; i < nums.length; i++){
                    if(nums[init] + nums[i] == target){
                        result[0] = init;
                        result[1] = i;
                    }
                }
                init++;
            }
            return result;
        }
    }
}
