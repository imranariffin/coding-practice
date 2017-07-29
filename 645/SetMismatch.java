import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;
import java.util.stream.IntStream;

public class SetMismatch {
	public static int[] findErrorNums(int[] nums) {
		int twice = -1;
		Set s = new HashSet<Integer>();
		for (int x: nums) {
			if (s.contains(x)) {
				twice = x;
				s.remove(x);
			} else {
				s.add(x);
			}
		}

		Set<Integer> v = new HashSet<Integer>(
			Arrays.asList(
				IntStream.range(1, nums.length + 1)
					.boxed()
					.toArray(
						Integer[]::new)));

		v.removeAll(s);
		int[] ret = v.stream().mapToInt(Integer::intValue).toArray();

		// make sure ret = [<twice>, <missing>]
		if (ret[0] == twice) {
			return ret;
		}
		// swap
		int temp = ret[0];
		ret[0] = ret[1];
		ret[1] = temp;
		return ret;
	}

	public static void main(String[] args) {
		int[] nums = {1, 3, 3};
		System.out.println(Arrays.toString(findErrorNums(nums)));
	}
}