import java.util.Arrays;

public class SearchRange {
	public static int[] searchRange(int[] nums, int target) {
		int i = binSearch(nums, target),
			left = findLeftBound(nums, target, i),
			right = findRightBound(nums, target, i);

		int[] ret = new int[2];
		ret[0] = left;
		ret[1] = right;

		return ret;
	}

	private static int binSearch(int[] nums, int target) {
		int i = 0, j = nums.length;

		while (i < j) {
			int mid = i + (j - i) / 2;

			System.out.println(Arrays.toString(nums) + ", " + mid);

			if (nums[mid] == target) {
				return mid;
			} else if (i == j) {
				return -1;
			} else if (target < nums[mid]) {
				j = mid;
			} else {
				i = mid + 1;
			}
		}
		return -1;
	}

	private static int 
	findRightBound(int[] nums, int target, int i) {
		if (i == -1) return -1;
		int ret = i;
		while (i < nums.length && nums[i] == target) {ret = i; i++;}
		return ret;
	}

	private static int 
	findLeftBound(int[] nums, int target, int i) {
		if (i == -1) return -1;
		int ret = i;
		while (i >= 0 && nums[i] == target) {ret = i; i--;}
		return ret;
	}

	public static void main(String[] args) {
		/* binSearch TEST */
// {5, 7, 7, 8, 8, 10} 7 -> 1,2
		int[] nums = {5, 7, 7, 8, 8, 10};
		String printStr = "nums: %s, target: %s\n ans: %s\n exp: %s\n";
		int target = 7;
		int ans = binSearch(nums, target);
		int[] exp = {1, 2};
		System.out.format(printStr, Arrays.toString(nums), target, ans, Arrays.toString(exp));
// {5, 7, 7, 8, 8, 10} 5 -> 0
		target = 5;
		ans = binSearch(nums, target);
		int[] exp2 = {0};
		System.out.format(printStr, Arrays.toString(nums), target, ans, Arrays.toString(exp2));
// {5, 7, 8, 8, 10} 7 -> 1
		int[] nums3 = {5, 7, 8, 8, 10};
		target = 7;
		ans = binSearch(nums3, target);
		int[] exp3 = {1};
		System.out.format(printStr, Arrays.toString(nums3), target, ans, Arrays.toString(exp3));
// {5, 7, 8, 8, 10} 10 -> 4
		target = 10;
		ans = binSearch(nums3, target);
		int[] exp4 = {4};
		System.out.format(printStr, Arrays.toString(nums3), target, ans, Arrays.toString(exp4));
// {5, 7, 8, 8, 10} 11 -> -1
		target = 11;
		ans = binSearch(nums3, target);
		int[] exp5 = {-1};
		System.out.format(printStr, Arrays.toString(nums3), target, ans, Arrays.toString(exp5));
	}
}