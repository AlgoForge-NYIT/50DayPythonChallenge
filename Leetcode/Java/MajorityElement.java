import java.util.Arrays;
import java.util.Set;
import java.util.TreeMap;

public class MajorityElement {
    public int majorityElement(int[] nums) {
        // 1. sort the array:
        Arrays.sort(nums);
        // 2. use for loop to find it:
        int majority = nums[0];
        int currentCount = 1;
        int largestCount = 1;
        for(int i = 0; i < nums.length - 1; i++){
            // if they are equal, add the current count
            if(nums[i] == nums[i+1]){
                currentCount++;
            }else{
                currentCount = 1;
            }
            // if the current count is bigger than the largest one, swap
            if(currentCount > largestCount){
                largestCount = currentCount;
                majority = nums[i];
            }
        }

        return majority;
    }

    public int majorityElement2(int[] nums) {
        TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                // if the map has the value:
                map.replace(nums[i],map.get(nums[i])+1);
            }else{
                // first time appears in the map:
                map.put(nums[i],1);
            }
        }

        int highKey = 0;
        int highValue = 0;
        // loop to find the one with the most value:
        Set<Integer> keys = map.keySet();
        for(Integer key : keys){
            if(map.get(key) > highValue){
                highValue = map.get(key);
                highKey = key;
            }
        }

        return highKey;
    }
}
