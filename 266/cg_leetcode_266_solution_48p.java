public class Solution {
    public boolean canPermutePalindrome(String s) {
        HashSet<Character> S = new HashSet();
        
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            
            if (!S.contains(c)) {
                S.add(c);
            }
            else {
                S.remove(c);
            }
        }
        
        boolean res = false;
        
        if (S.size() < 2) {
            res = true;
        }
        
        return res;
    }
}
