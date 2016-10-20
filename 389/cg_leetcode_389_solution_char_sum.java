public class Solution {
    public char findTheDifference(String s, String t) {
        int S = 0;
        int T = 0;
        
        for (int i = 0; i < s.length(); i++) {
            S += s.charAt(i);
        }
        
        for (int i = 0; i < t.length(); i++) {
            T += t.charAt(i);
        }
        
        return T - S;
    }
}
