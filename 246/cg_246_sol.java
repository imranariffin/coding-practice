public class Solution {
    public boolean isStrobogrammatic(String num) {
        int p0 = 0;
        int p1 = num.length() - 1;
        
        while (p0 <= p1) {
            
            if (!isStrobo(num.charAt(p0), num.charAt(p1))) {
                return false;
            }
            
            p0 += 1;
            p1 -= 1;
        }
        
        return true;
    }
    
    private boolean isStrobo(char c0, char c1) {
        if (c0 == '1' && c1 == '1') {
            return true;
        }
        else if (c0 == '8' && c1 == '8') {
            return true;
        }
        else if (c0 == '6' && c1 == '9') {
            return true;
        }
        else if (c0 == '9' && c1 == '6') {
            return true;
        }
        else if (c0 == '0' && c1 == '0') {
            return true;
        }
        
        return false;
    }
}
