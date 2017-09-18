class Solution {    
    public boolean validPalindrome(String str) {
        char[] s = str.toCharArray();
        if (valid(s)) {
            return true;
        }

        int i, j;
        for (i = 0, j = s.length - 1; j >= 0; i++, j--) {
            char a = s[i]; char b = s[j];
            if (a != b) {
                char[] t1 = (str.substring(0, i) + str.substring(i + 1)).toCharArray();
                if (valid(t1)) {
                    return true;
                }
                char[] t2 = (str.substring(0, j) + str.substring(j + 1)).toCharArray();
                if (valid(t2)) {
                    return true;
                }
                return false;
            }
        }
        
        return false;
    }
    
    private boolean valid(char[] s) {
        int i, j;
        for (i = 0, j = s.length - 1; j >= 0; i++, j--) {
            char a = s[i]; char b = s[j];
            if (a != b) {
                return false;
            }
        }
        return true;
    }
}
