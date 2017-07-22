import java.util.Arrays;

public class SearchInsert {
	public static int searchInsert(int[] nums, int target) {
		if (nums == null || nums.length == 0) {
			return 0;
		}
		return binSearchInsert(nums, target, 0, nums.length - 1);
	}

	private static int 
	binSearchInsert(int[] nums, int target, int s, int e) {
		int i = (s + e) / 2;
		if (target < nums[i]) {
			if (s == e - 1 || s == e) {
				return i;
			}
			return binSearchInsert(nums, target, s, i);
		} else if (target > nums[i]) {
			if (s == e) {
				return i + 1;
			}
			return binSearchInsert(nums, target, i + 1, e);
		}
		return i;
	}

	public static void main(String[] args) {
		int target, ans, exp;
		String printStr = "nums: %s, target: %s\n ans: %s\n expected: %s\n";
// [1,3,5,6], 5 → 2
		int nums[] = {1,3,5,6};
		target = 5;
		exp = 2;
		ans = searchInsert(nums, target);
		System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// [1,3,5,6], 2 → 1
		target = 2;
		exp = 1;
		ans = searchInsert(nums, target);
		System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// [1,3,5,6], 7 → 4
		target = 7;
		exp = 4;
		ans = searchInsert(nums, target);
		System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// [1,3,5,6], 0 → 0
		target = 0;
		exp = 0;
		ans = searchInsert(nums, target);
		System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// [1,3,5,9], 7 → 3
		int nums2[] = {1,3,5,9};
		target = 7;
		exp = 3;
		ans = searchInsert(nums2, target);
		System.out.format(printStr, Arrays.toString(nums2), target, ans, exp);
// [1,3,6,9], 5 → 2
		int nums3[] = {1,3,6,9};
		target = 5;
		exp = 2;
		ans = searchInsert(nums3, target);
		System.out.format(printStr, Arrays.toString(nums3), target, ans, exp);
// [1,3,7,9,11], 12 → 5
		int nums4[] = {1,3,7,9,11};
		target = 12;
		exp = 5;
		ans = searchInsert(nums4, target);
		System.out.format(printStr, Arrays.toString(nums4), target, ans, exp);
	}
}