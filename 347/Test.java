import java.util.List;

class Test {
	public static void main(String[] args) {
		Solution s = new Solution();

		System.out.println("Test 0");
		int[] nums0 = new int[] {1,1,1,2,2,3};
		int k0 = 2;
		int[] ans0 = new int[] {1,2};
		List<Integer> ret0 = s.topKFrequent(nums0, k0);
		for (int i=0; i<k0; i++) {
			assert ans0[i] == ret0.get(i);
		}
	}
}