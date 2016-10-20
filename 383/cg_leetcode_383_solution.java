public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> m = new HashMap<Character, Integer>();
        
        for (int i = 0; i < magazine.length(); i++) {
            Character c = magazine.charAt(i);
            
            if (m.containsKey(c)) {
                m.put(c, m.get(c) + 1);
            }
            else {
                m.put(c, 1);
            }
        }
        
        for (int i = 0; i < ransomNote.length(); i++) {
            Character c = ransomNote.charAt(i);
            
            if (m.containsKey(c) && m.get(c) > 0) {
                m.put(c, m.get(c) - 1);
            }
            else {
                return false;
            }
        }
        
        return true;
    }
}
