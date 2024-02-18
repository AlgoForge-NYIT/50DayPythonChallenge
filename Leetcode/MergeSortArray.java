import java.util.Arrays;

public class MergeSortArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int counter = 0;
        for(int i = 0; i < nums1.length; i++){
            if(nums1[i] == 0 && nums2.length > 0){
                if(counter == n) break;
                nums1[i] = nums2[counter];
                counter++;
            }
        }
        Arrays.sort(nums1);
    }
}
