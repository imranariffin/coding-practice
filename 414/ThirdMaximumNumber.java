import java.util.Arrays;

public class ThirdMaximumNumber {
	public static int thirdMax(int[] nums) {
		Integer max = null;
		Integer max2 = null;
		Integer max3 = null;

		for (Integer e: nums) {
			if (!e.equals(max) && !e.equals(max2) && !e.equals(max3)) {
				if (max == null || e > max) {
					max3 = max2;
					max2 = max;
					max = e;
				} else if (max2 == null || e > max2) {
					max3 = max2;
					max2 = e;
				} else if (max3 == null || e > max3) {
					max3 = e;
				}
			}
		}
		return max3 == null ? max : max3;
	}

	public static void main(String[] args) {
		int[] nums = {1,2,3,4,5};
		int ans = thirdMax(nums);
		int exp = 3;
		String print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums), ans, exp);

		int[] nums2 = {1,2,3,4,4,5};
		ans = thirdMax(nums2);
		exp = 3;
		print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums2), ans, exp);

		int[] nums3 = {1,2,};
		ans = thirdMax(nums3);
		exp = 2;
		print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums3), ans, exp);

		int[] nums4 = {2,2,3,1};
		ans = thirdMax(nums4);
		exp = 1;
		print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums4), ans, exp);

		int[] nums5 = {2,2,1};
		ans = thirdMax(nums5);
		exp = 2;
		print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums5), ans, exp);

		int[] nums6 = {1,2,-2147483648};
		ans = thirdMax(nums6);
		exp = -2147483648;
		print = "nums: %s\nAns: %s\nExpected: %s\n";
		System.out.format(print, Arrays.toString(nums6), ans, exp);
	}
}