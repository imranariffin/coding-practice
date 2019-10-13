public class Solution {
    public int myAtoi(String str) {
        str = str.trim();
        
        if (str.length() < 1) {
            return 0;
        }
        
        boolean isNeg = false;
        
        if (str.charAt(0) == '+' || str.charAt(0) == '-') {
            isNeg = str.charAt(0) == '-' ? true : false;
            str = str.substring(1);
        }
        
        if (str.length() < 1 || (str.charAt(0) == '+' || str.charAt(0) == '-')) {
            return 0;
        }
        
        int p = 0;
        
        while (p < str.length() && str.charAt(p) >= '0' && str.charAt(p) <= '9') {
            p++;
        }
        
        str = str.substring(0, p);
        
        if (str.length() < 1) {
            return 0;
        }
        
        long val = 0;
        int mul = (int) Math.pow(10, str.length() - 1);
        
        for (int i = 0; i < str.length(); i++) {
            val += (long) (mul * (str.charAt(i) - '0'));
            mul /= 10;
        }
        
        val = isNeg ? -1 * val : val;
        
        if (val > Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        }
        
        if (val < Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }
        
        return (int) val;
    }
}
