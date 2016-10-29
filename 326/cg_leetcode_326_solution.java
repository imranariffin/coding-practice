public class Solution {
    public boolean isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        }
        
        return recurse(n);
    }
    
    private boolean recurse(int x) {
        if (x == 1) {
            return true;
        }
        
        if (x % 3 == 0) {
            return recurse(x / 3);
        }
        else {
            return false;
        }
    }
}
