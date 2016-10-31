public class Solution {
    public boolean isUgly(int num) {
        if (num <= 0) {
            return false;
        }
        
        int[] uglyPrimeFactors = new int[] { 2, 3, 5 };
        
        while (num != 1) {
            boolean ugly = false;
            
            for (int uglyPrime : uglyPrimeFactors) {
                if (num % uglyPrime == 0) {
                    ugly = true;
                    num /= uglyPrime;
                }
            }
            
            if (!ugly) {
                return false;
            }
        }
        
        return true;
    }
}
