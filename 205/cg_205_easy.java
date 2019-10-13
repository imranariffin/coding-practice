public class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> m = new HashMap<>();
        Set<Character> S = new HashSet<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (!m.containsKey(s.charAt(i)) && !S.contains(t.charAt(i))) {
                m.put(s.charAt(i), t.charAt(i));
                S.add(t.charAt(i));
            }
            
            if (!m.containsKey(s.charAt(i)) || t.charAt(i) != m.get(s.charAt(i))) {
                return false;
            }
        }
        
        return true;
    }
}
