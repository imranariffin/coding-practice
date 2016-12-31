public class Solution {
    public String convertToTitle(int n) {
        if (n < 1) {
            return "";
        }
        
        int x = n - 1;
        StringBuilder sb = new StringBuilder();
        
        while (x > 25) {
            sb.append(getLetter(x % 26));
            x = (x / 26) - 1;
        }
        
        sb.append(getLetter(x));
        
        return sb.reverse().toString();
    }
    
    private char getLetter(int num) {
        if (num < 0 || num > 25) {
            return '?';
        }
        
        return (char) (num + 'A');
    }
}
