public class Solution {
    public boolean isPalindrome(int x) {
        String xString = Integer.toString(x);
        
        int p0 = 0;
        int p1 = xString.length() - 1;
        
        while (p0 < p1) {
            if (xString.charAt(p0) != xString.charAt(p1)) {
                return false;
            }
            
            p0++;
            p1--;
        }
        
        return true;
    }
}
