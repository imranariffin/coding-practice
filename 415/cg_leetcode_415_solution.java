public class Solution {
    public String addStrings(String num1, String num2) {
        if (num1.length() < num2.length()) {
            return addStrings(num2, num1);
        }
        
        int p1 = num1.length() - 1;
        int p2 = num2.length() - 1;
        int carry = 0;
        StringBuilder sb = new StringBuilder();
        
        while (p2 >= 0) {
            int add = (num1.charAt(p1) - '0') + (num2.charAt(p2) - '0') + carry;
            
            carry = add / 10;
            add = add % 10;
            
            sb.append(add);
            
            p1 -= 1;
            p2 -= 1;
        }
        
        while (p1 >= 0) {
            int add = (num1.charAt(p1) - '0') + carry;
            
            carry = add / 10;
            add = add % 10;
            
            sb.append(add);
            
            p1 -= 1;
        }
        
        if (carry > 0) {
            sb.append(carry);
        }
        
        sb = sb.reverse();
        
        return sb.toString();
    }
}
