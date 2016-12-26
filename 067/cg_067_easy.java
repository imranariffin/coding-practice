public class Solution {
    public String addBinary(String a, String b) {
        int pA = a.length() - 1;
        int pB = b.length() - 1;
        char carry = '0';
        StringBuilder sb = new StringBuilder();
        
        while (pA >= 0 || pB >= 0) {
            char currA = pA >= 0 ? a.charAt(pA) : '0';
            char currB = pB >= 0 ? b.charAt(pB) : '0';
            char y = add(currA, currB);
            
            y = add(y, carry);
            sb.append(y);
            
            int c = 0;
            
            c += currA == '1' ? 1 : 0;
            c += currB == '1' ? 1 : 0;
            c += carry == '1' ? 1 : 0;
            carry = c > 1 ? '1' : '0';
            
            pA--;
            pB--;
        }
        
        if (carry == '1') {
            sb.append(carry);
            carry = '0';
        }
        
        return sb.reverse().toString();
    }
    
    private char add(char a, char b) {
        if (a == '1' && b == '1' || a == '0' && b == '0') {
            return '0';
        }
        
        if (a == '1' && b == '0' || a == '0' && b == '1') {
            return '1';
        }
        
        return '?';
    }
    
    private char getCarry(char a, char b) {
        if (a == '1' && b == '1') {
            return '1';
        }
        
        if (a == '0' && b == '0' || a == '1' && b == '0' || a == '0' && b == '1') {
            return '1';
        }
        
        return '?';
    }
}
