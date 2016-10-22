public class Solution {
    public int firstUniqChar(String s) {
        int[] h = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            h[s.charAt(i) - 'a'] += 1;
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (h[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
