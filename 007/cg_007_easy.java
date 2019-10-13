public class Solution {
    public int reverse(int x) {
        boolean neg = x < 0 ? true : false;
        StringBuilder sb = new StringBuilder(Integer.toString(neg ? x * -1 : x));
        String s = trimLeadingZero(sb.reverse().toString());
        int res = 0;
        
        try {
            res = !s.isEmpty() ? Integer.parseInt(s) : 0;
        }
        catch (Exception ex) {
            return res;
        }
        
        return neg ? res * -1 : res;
    }
    
    private String trimLeadingZero(String s) {
        int p = 0;
        
        while (p < s.length() && s.charAt(p) == '0') {
            p++;
        }
        
        return p < s.length() ? s.substring(p) : "";
    }
}
