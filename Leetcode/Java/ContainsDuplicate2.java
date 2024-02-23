import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate2 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k){
                // remove the first one of the window
                set.remove(nums[i-k-1]);
            }
            // if adding an integer to the set return false,
            // duplicated found and return true;
            if(!set.add(nums[i])){
                return true;
            }
        }
        // if above conditions don't meet, return false;
        return false;
    }
}
