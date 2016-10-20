public class Solution {
    public char findTheDifference(String s, String t) {
        HashMap<Character, Integer> S = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            
            if (S.containsKey(c)) {
                S.put(c, S.get(c) + 1);
            }
            else {
                S.put(c, 1);
            }
        }
        
        HashMap<Character, Integer> T = new HashMap<Character, Integer>();
        
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            
            if (T.containsKey(c)) {
                T.put(c, T.get(c) + 1);
            }
            else {
                T.put(c, 1);
            }
        }
        
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            
            if (!S.containsKey(c) || S.get(c) != T.get(c)) {
                return c;
            }
        }
        
        return '?';
    }
}
