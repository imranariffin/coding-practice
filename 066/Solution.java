public class Solution {
    public int[] plusOne(int[] digits) {
        return this.plusN(digits, 1);
    }
    
    private int[] plusN(int[] digits, int n) {
        int[] ret = new int[digits.length];
        int carry = n;
        
        for (int i=digits.length-1; i>=0; i--) {
            ret[i] = (digits[i] + carry)%10;
            if (carry!=0)
                carry = (digits[i]+1)/10;
        }
        
        if (carry!=0) {
            int[] new_ret = new int [ret.length + 1];
            new_ret[0] = carry;
            for (int i=0; i<ret.length; i++) {
                new_ret[i+1] = ret[i];
            }
            return new_ret;
        }
         
        return ret;   
    }
}