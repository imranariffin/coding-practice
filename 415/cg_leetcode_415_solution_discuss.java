public class Solution {

    // "https://discuss.leetcode.com/topic/62310/straightforward-java-10-main-lines-25ms".
    public String addStrings(String num1, String num2) {
        int carry = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int i1 = num1.length() - 1, i2 = num2.length() - 1; i1 >= 0 || i2 >= 0; i1--, i2--) {
            int a = i1 < 0 ? 0 : num1.charAt(i1) - '0';
            int b = i2 < 0 ? 0 : num2.charAt(i2) - '0';
            int abc = a + b + carry;
            
            carry = abc / 10;
            abc %= 10;
            
            sb.append(abc);
        }
        
        if (carry > 0) {
            sb.append(carry);
        }
        
        return sb.reverse().toString();
    }
}
