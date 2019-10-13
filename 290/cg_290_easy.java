public class Solution {
    public boolean wordPattern(String pattern, String str) {
        Map<Character, String> m = new HashMap<>();
        String[] strArr = str.split(" ");
        Set<String> s = new HashSet<String>();
        
        if (pattern.length() != strArr.length) {
            return false;
        }
        
        for (int i = 0; i < pattern.length(); i++) {
            Character ch = pattern.charAt(i);
            
            if (!m.containsKey(ch) && !s.contains(strArr[i])) {
                m.put(ch, strArr[i]);
                s.add(strArr[i]);
            }
            
            if (!m.containsKey(ch) || !strArr[i].equals(m.get(ch))) {
                return false;
            }
        }
        
        return true;
    }
}
