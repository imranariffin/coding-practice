public class Solution {
    public int findPairs(int[] nums, int k) {
        if (k < 0) return 0;

        int pairCount = 0;
        HashSet<Integer> s = new HashSet<>();
        Map<Integer, Integer> m = new HashMap<>();

        for (int num : nums) {
            s.add(num);
            m.put(num, m.getOrDefault(num, 0) + 1);
        }

        List<Integer> l = new ArrayList<>(s);
        l.sort((a, b) -> a.compareTo(b));

        for (int num : l) {
            int c = num + k;

            if (m.containsKey(c)) {
                if (c != num || m.get(c) > 1) {
                    //System.out.printf("%d, %d\n", num, c);
                    pairCount += 1;
                }
            }
        }

        return pairCount;
    }
}
