public class Solution {
	public int numTrees(int n) {
		if (n <= 0) return 0;

		int[] mem = new int[n];
		return helper(n, mem);
	}

	private int helper(int n, int[] mem) {

		if (n == 0)
			return 1;
		if (mem[n-1] != 0) 
			return mem[n-1];

		int sum = 0;
		for (int i=1; i<=n; i++) {
			sum += 
				helper(i-1, mem)
					*
				helper(n-i, mem);
		}

		mem[n-1] = sum;
		return sum;
	}
}