public class Solution {
    public int titleToNumber(String s) {
        if (s.length() < 1) {
            return 0;
        }
        
        int res = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            res += (cToInt(c) * Math.pow(26, s.length() - 1 - i));
        }
        
        return res;
    }
    
    private int cToInt(char c) {
        if (c < 'A' || c > 'Z') {
            return -1;
        }
        
        return c - 'A' + 1;
    }
}
