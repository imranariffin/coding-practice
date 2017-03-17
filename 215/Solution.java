import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Comparator;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
    	Integer[] iNums = new Integer[nums.length];
    	for (int i = 0; i < nums.length; i++) {
    		iNums[i] = nums[i];
    	}

        PriorityQueue<Integer> maxHeap = 
        	new PriorityQueue<Integer>(
        		new Comparator<Integer>() {
        			public int compare(Integer x, Integer y) {
        				return y - x;
        			}
        		});
        maxHeap.addAll(new ArrayList<Integer>(Arrays.asList(iNums)));

        Integer i = new Integer(0);
        Integer kMax = maxHeap.peek();
        while (i < k) {
        	kMax = maxHeap.poll();
        	i++;
        }
        return kMax.intValue();
    }

    public static void main(String[] args) {
    	Solution s = new Solution();

    	System.out.println("TEST 0");
    	int[] nums0 = {3,2,1,5,6,4};
    	int k0 = 2;
    	System.out.println(Arrays.toString(nums0) + ", " + k0);
    	System.out.println(s.findKthLargest(nums0, k0));

   		System.out.println("TEST 1");
    	int[] nums1 = {3,2,1,5,6,4};
    	int k1 = 6;
    	System.out.println(Arrays.toString(nums1) + ", " + k1);
    	System.out.println(s.findKthLargest(nums1, k1));

    	System.out.println("TEST 2");
    	int[] nums2 = {3,2,1,5,6,4};
    	int k2 = 0;
    	System.out.println(Arrays.toString(nums2) + ", " + k2);
    	System.out.println(s.findKthLargest(nums2, k2));
    }
}