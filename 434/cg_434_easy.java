public class Solution {
    public int countSegments(String s) {
        int segment = 0;
        boolean valid = false;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                if (valid) {
                    segment++;
                }
                
                valid = false;
            }
            else {
                valid = true;
            }
        }
        
        if (valid) {
            segment++;
            valid = false;
        }
        
        return segment;
    }
}
