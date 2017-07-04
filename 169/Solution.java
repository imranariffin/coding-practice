import java.util.HashMap;
import java.util.Iterator;
import java.util.Arrays;

public class Solution {
	public int majorityElement(int[] nums) {
		HashMap<Integer, Integer>
			freqs = new HashMap<Integer, Integer>();
		int N = nums.length;

		for(int i=0; i<N; i++) {
			int n = nums[i];

			if (!(freqs.containsKey(n))) {
				freqs.put(n, 1);
			}
			else {
				freqs.put(n, freqs.get(n)+1);
			}
		}

        int hf = N/2;
		for (int i=0; i<N; i++) {
			int n = nums[i];
			if (freqs.get(n) > hf)
				return n;
		}
		return -1;
	}
	
	public static void
	main(String[] args) {
		Solution s = new Solution();

		System.out.println("TEST 0");
		int[] nums0 = {1, 2, 3, 4, 5};
		System.out.println(Arrays.toString(nums0));
		System.out.println(s.majorityElement(nums0));

		System.out.println("TEST 1");
		int[] nums1 = {1, 1, 1, 4, 5};
		System.out.println(Arrays.toString(nums1));
		System.out.println(s.majorityElement(nums1));

		System.out.println("TEST 2");
		int[] nums2 = {1, 2, 3, 5, 5, 5};
		System.out.println(Arrays.toString(nums2));
		System.out.println(s.majorityElement(nums2));

		System.out.println("TEST 3");
		int[] nums3 = {1, 2, 3, 5, 5, 5, 6, 6, 6, 6, 6};
		System.out.println(Arrays.toString(nums3));
		System.out.println(s.majorityElement(nums3));

		System.out.println("TEST 4");
		int[] nums4 = {1, 1, 3, 5, 5};
		System.out.println(Arrays.toString(nums4));
		System.out.println(s.majorityElement(nums4));

		return;
	}
}