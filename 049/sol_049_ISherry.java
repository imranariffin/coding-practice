public class Solution {

    int[] primes = new int[] { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109 };

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<String>> hm = new HashMap<>();
        for (String s : strs) {
            Integer h = new Integer(hash(s));
            List<String> nv = hm.getOrDefault(h, new LinkedList<>());
            nv.add(s);
            hm.put(h, nv);
        }
        return hm.values().stream().collect(Collectors.toList());
    }

    private int hash(String s) {
        int hval = 1;
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            hval *= primes[c - 'a'];
        }
        return hval;
    }
}
