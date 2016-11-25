public class Solution {
    public String getHint(String secret, String guess) {
        int length = secret.length() == guess.length() ? secret.length() : 0;
        
        int a = 0;
        
        for (int i = 0; i < length; i++) {
            a += secret.charAt(i) == guess.charAt(i) ? 1 : 0;
        }
        
        int b = 0;
        Map<Character, Integer> m = new HashMap<>();
        
        for (int i = 0; i < length; i++) {
            char ch = secret.charAt(i);
            
            m.put(ch, m.getOrDefault(ch, 0) + 1);
        }
        
        for (int i = 0; i < guess.length(); i++) {
            char ch = guess.charAt(i);
            
            if (m.containsKey(ch) && m.get(ch) > 0) {
                m.put(ch, m.get(ch) - 1);
                b += 1;
            }
        }
        
        b -= a;
        
        return a + "A" + b + "B";
    }
}
