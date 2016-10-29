public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n < 1) {
            return false;
        }
        
        double pow = Math.log(n) / Math.log(2);
        
        return Math.abs(pow - Math.round(pow)) < 0.000000000001 ? true : false;
    }
}
