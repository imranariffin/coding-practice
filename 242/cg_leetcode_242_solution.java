public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() == 0 && t.length() == 0) {
            return true;
        }
        
        if (s.length() != t.length()) {
            return false;
        }
        
        ArrayList<Character> S = new ArrayList<Character>();
        ArrayList<Character> T = new ArrayList<Character>();
        
        for (int i = 0; i < s.length(); i++) {
            S.add(s.charAt(i));
        }
        
        for (int i = 0; i < t.length(); i++) {
            T.add(t.charAt(i));
        }
        
        S.sort((x, y) -> x - y);
        T.sort((x, y) -> x - y);
        
        for (int i = 0; i < S.size(); i++) {
            if (S.get(i) != T.get(i)) {
                return false;
            }
        }
        
        return true;
    }
}
