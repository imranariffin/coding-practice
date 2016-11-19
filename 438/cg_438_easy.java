public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] want = new int[26];
        int head = 0;
        int tail = 0;
        int complete = p.length();
        List<Integer> res = new ArrayList<>();
        
        for (char chr : p.toCharArray()) {
            want[chr - 'a']++;
        }
        
        while (tail < s.length()) {
            // If we found the character that we are looking for, decrement our want.
            if (want[s.charAt(tail++) - 'a']-- > 0) {
                complete--;
            }
            
            // We satisfy the substring requirement every time complete hits 0.
            if (complete == 0) {
                res.add(head);
            }
            
            // First, check for sliding window size. We need to increment head
            // when the window size gets too big. Second, increment our want since
            // we are removing the character out of our sliding window. Actual wanted
            // characters will always be >= 0 and unwanted characters will always be
            // -1 before any increment is done to it. We will never increment complete
            // for unwanted characters.
            if (tail - head >= p.length() && want[s.charAt(head++) - 'a']++ >= 0) {
                complete++;
            }
        }
        
        return res;
    }
}
