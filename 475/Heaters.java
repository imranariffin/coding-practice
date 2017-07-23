import java.util.Arrays;

public class Heaters {
	public static int findRadius(int[] houses, int[] heaters) {
		Arrays.sort(heaters);

		int rad = Integer.MIN_VALUE;
		for (int i: houses) {
			int index = Arrays.binarySearch(heaters, i);
			if (index < 0) {
				index = -(index + 1);
			}

			int leftDist = index - 1 >= 0 ? i - heaters[index - 1] : Integer.MAX_VALUE;
			int rightDist = index < heaters.length ? heaters[index] - i : Integer.MAX_VALUE;

			rad = Math.max(rad, Math.min(leftDist, rightDist));
		}

		return rad;
	}

	public static void main(String[] args) {
		int[] houses = {1,2,3}, heaters = {2};
		int exp = 1;
		int ans = findRadius(houses, heaters);
		String printStr = "houses: %s, heaters: %s\n exp: %s\n ans: %s\n";
		System.out.format(printStr, 
			Arrays.toString(houses), 
			Arrays.toString(heaters),
			exp, ans);
	}
}