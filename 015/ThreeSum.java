import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

class Triplet {
	public int a;
	public int b;
	public int c;
	public Triplet(int _a, int _b, int _c) {
		int[] arr = {_a, _b, _c};
		Arrays.sort(arr);
		a = arr[0]; 
		b = arr[1]; 
		c = arr[2];
	}
	public int[] toArray() {
		int[] ret = new int[3];
		ret[0] = a; ret[1] = b; ret[2] = c;
		return ret;
	}
	public String toString() {
		return "("+a+","+b+","+c+")";
	}
}

public class ThreeSum {
	public static List<List<Integer>> threeSum(int[] nums) {
		if (nums == null || nums.length == 0) {
			return new ArrayList<>();
		}

		Map<String,Triplet> retMap = new HashMap<>();
		Arrays.sort(nums);
		for (int i=0; i<nums.length; i++) {
			int s = i + 1;
			int e = nums.length - 1;
			while (s < e) {
				int a = nums[s];
				int b = nums[i];
				int c = nums[e];
				int sum = a + b + c;
				if (sum == 0) {
					Triplet triplet = new Triplet(a, b, c);
					if (!retMap.containsKey(triplet.toString())) {
						retMap.put(triplet.toString(), triplet);
					}
					s++;
					e--;
				} else if (sum > 0) {
					e--;
				} else {
					s++;
				}
			}
		}
		List<List<Integer>> ret = new ArrayList<>();
		for (Triplet triplet: retMap.values()) {
			List<Integer> list = new ArrayList<>();
			list.add(triplet.a);
			list.add(triplet.b);
			list.add(triplet.c);
			ret.add(list);
		}
		return ret;
	}

	public static void main(String[] args) {
		int[] nums = {1,2,1,1,1};
		String prntstr = "%s\nAns: %s\nExp: %s\n";
		List<List<Integer>> ret = threeSum(nums);
		String exp = "[]";
		System.out.format(prntstr, 
			Arrays.toString(nums), ret, exp);

		int[] nums2 = {-1,0,1,2,-1,-4};
		ret = threeSum(nums2);
		exp = "[[-1, -1, 2], [-1, 0, 1]]";
		System.out.format(prntstr, 
			Arrays.toString(nums2), ret, exp);
	}
}