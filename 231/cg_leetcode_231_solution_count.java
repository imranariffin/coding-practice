public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n < 1) {
            return false;
        }
        
        int count = 0;
        String s = Integer.toBinaryString(n);
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                count++;
            }
            
            if (count > 1) {
                return false;
            }
        }
        
        return true;
    }
}
