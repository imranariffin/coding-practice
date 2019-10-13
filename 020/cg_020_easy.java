public class Solution {
    Character[] openings = new Character[] { '(', '[', '{' };
    Character[] closings = new Character[] { ')', ']', '}' };
    
    public boolean isValid(String s) {
        Deque<Character> S = new ArrayDeque<>();
        
        for (char ch : s.toCharArray()) {
            if (isOpening(ch)) {
                S.push(ch);
                
                continue;
            }
            
            if (S.isEmpty() || ch != getClosing(S.pop())) {
                return false;
            }
        }
        
        return S.isEmpty() ? true : false;
    }
    
    private Character getClosing(Character ch) {
        for (int i = 0; i < openings.length; i++) {
            if (openings[i] == ch) {
                return closings[i];
            }
        }
        
        return ch;
    }
    
    private boolean isOpening(Character ch) {
        for (int i = 0; i < openings.length; i++) {
            if (openings[i] == ch) {
                return true;
            }
        }
        
        return false;
    }
}
