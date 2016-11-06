public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        HashMap<String, List<String>> groups = new HashMap<String, List<String>>();
        
        for (int i = 0; i < strings.length; i++) {
            String group = normalize(strings[i]);
            
            if (!groups.containsKey(group)) {
                groups.put(group, new ArrayList<String>());
            }
            
            groups.get(group).add(strings[i]);
            
            // System.out.printf("group: %s, string: %s\n", group, strings[i]);
        }
        
        return new ArrayList<List<String>>(groups.values());
    }
    
    private String normalize(String s) {
        if (s.length() < 1) {
            return "";
        }
        
        int offset = 'z' - s.charAt(0);
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c + offset > 'z') {
                c = intToChar('a' + offset - ('z' - c) - 1);  // Why do we need to -1 again?
            }
            else {
                c = intToChar(c + offset);
            }
            
            sb.append(c);
        }
        
        return sb.toString();
    }
    
    private char intToChar(int a) {
        if (a < 'a' || a > 'z') {
            return '!';
        }
        
        return (char) a;
    }
}
