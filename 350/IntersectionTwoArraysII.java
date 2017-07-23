import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;

public class IntersectionTwoArraysII {
	public static int[] intersect(int[] nums1, int[] nums2) {
		if (nums2.length < nums1.length) {
			int[] temp = nums1;
			nums1 = nums2;
			nums2 = temp;
		}

		Map hm = new HashMap<Integer, Integer>();
		for (int x: nums1) {
			if (!hm.containsKey(x)) {
				hm.put(x, 1);
			} else {
				hm.put(x, ((Integer) hm.get(x)) + 1);
			}
		}

		List<Integer> ret = new ArrayList<Integer>();
		for (int x: nums2) {
			if (hm.containsKey(x)) {
				ret.add(x);
				int f = ((Integer) hm.get(x)) - 1;
				hm.put(x,  f);
				if (f == 0) {
					hm.remove(x);
				}
			}
		}
		
		return ret.stream().mapToInt(i->i).toArray();

		// Map intx = new HashMap<Integer, Integer>();
		// int intxCount = 0;

		// for (int n: nums2) {
		// 	if (s.contains(n)) {
		// 		intxCount++;
		// 		if (!intx.containsKey(n)) {
		// 			intx.put(n, 1);
		// 		} else {
		// 			intx.put(n, ((Integer) intx.get(n)) + 1);
		// 		}
		// 	}
		// }

		// int[] ret = new int[intxCount];
		// int i = 0;
		// Iterator it = intx.keySet().iterator();
		// while (it.hasNext()) {
		// 	Integer n = (Integer) it.next();
		// 	Integer f = (Integer) intx.get(n);
		// 	for (Integer j = 0; j < f; j++) {
		// 		ret[i++] = n;
		// 	}
		// }

		// return ret;
	}

	public static void main(String[] args) {
		int[] nums1 = {1, 2, 1, 2};
		int[] nums2 = {2, 2};
		System.out.println(Arrays.toString(intersect(nums1, nums2)));

		int[] nums1_2 = {1, 2, 1, 2, 3, 3, 3, 5};
		int[] nums2_2 = {2, 2, 3};
		System.out.println(Arrays.toString(intersect(nums1_2, nums2_2)));
	}
}