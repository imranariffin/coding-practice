public class Solution {
    public String countAndSay(int n) {
        if (n == 0) {
            return "";
        }
        
        String s = "1";
        
        for (int i = 1; i < n; i++) {
            s = say(s);
        }
        
        return s;
    }
    
    private String say(String s) {
        if (s.length() < 1) {
            return "";
        }
        
        if (s.length() == 1) {
            return "1" + s;
        }
        
        int count = 1;
        StringBuilder sb = new StringBuilder();
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            }
            else {
                sb.append(count);
                sb.append(s.charAt(i - 1));
                count = 1;
            }
        }
        
        sb.append(count);
        sb.append(s.charAt(s.length() - 1));
        
        return sb.toString();
    }
}
