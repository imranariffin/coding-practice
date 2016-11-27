public class Solution {
    /**
     * Refer "https://discuss.leetcode.com/topic/69722/java-solution-in-linear-time".
     * 
     * Consider s="ab" and t="aa". If s is the key, we will produce a map of a: a, b: a.
     * To get around that, make t to be the key. This will produce a map of a: a and b, which
     * is wrong.
     * 
     */
    public boolean isIsomorphic(String s, String t) {
        return check(s, t) && check(t, s);
    }
    
    private boolean check(String s, String t) {
        Map<Character, Character> m = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (!m.containsKey(s.charAt(i))) {
                m.put(s.charAt(i), t.charAt(i));
            }
            
            if (m.get(s.charAt(i)) != t.charAt(i)) {
                return false;
            }
        }
        
        return true;
    }
}
