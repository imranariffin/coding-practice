public class Solution {
    public boolean repeatedSubstringPattern(String str) {
        for (int i = 1; i <= str.length() / 2; i++) {
            if (str.length() % i != 0) {
                continue;
            }
            
            boolean repeating = true;
            
            for (int j = 0; j < str.length(); j += i) {
                if (!str.substring(j, j + i).equals(str.substring(0, i))) {
                    repeating = false;
                }
            }
            
            if (repeating) {
                return true;
            }
        }
        
        return false;
    }
}
