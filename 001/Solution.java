import java.util.Arrays;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        int[] ret = new int[2];
        int m, n;

        for (int i=0; i<len; i++) {
        	m = nums[i];
        	for (int j=i+1; j<len; j++) {
        		n = nums[j];
        		if ((m + n) == target) {
        			ret[0] = i; ret[1] = j;
        			return ret;
        		}
        	}
        }
        return ret;
    }

    public static void
    main(String[] args) {

    	Solution
    	s = new Solution();

    	System.out.println(" --- TEST --- ");

    	System.out.println("TEST 0");
    	int[] nums0 = {1, 2, 3, 4};
    	int target0 = 6;
    	System.out.println("nums= " + Arrays.toString(nums0) + ", " + "target= " + target0);
    	System.out.println(Arrays.toString(s.twoSum(nums0, target0)));

    	System.out.println("TEST 1");
    	int[] nums1 = {-1, -2, -3, -4};
    	int target1 = -3;
    	System.out.println("nums= " + Arrays.toString(nums1) + ", " + "target= " + target1);
    	System.out.println(Arrays.toString(s.twoSum(nums1, target1)));

    	return;
    }
}