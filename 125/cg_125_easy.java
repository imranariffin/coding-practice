public class Solution {
    public boolean isPalindrome(String s) {
        int a = 0;
        int b = s.length() - 1;
        
        while (a < b) {
            if (!isValidCharacter(s.charAt(a))) {
                a++;
                
                continue;
            }
            
            if (!isValidCharacter(s.charAt(b))) {
                b--;
                
                continue;
            }
            
            if (!compare(s.charAt(a), s.charAt(b))) {
                return false;
            }
            
            a++;
            b--;
        }
        
        return true;
    }
    
    private boolean compare(char c0, char c1) {
        if (isNumeric(c0) && isNumeric(c1)) {
            if (c0 == c1) {
                return true;
            }
            
            return false;
        }
        else if (isLowerCaseLetter(c0) && isLowerCaseLetter(c1)) {
            if (c0 == c1) {
                return true;
            }
            
            return false;
        }
        else if (isCapitalLetter(c0) && isCapitalLetter(c1)) {
            if (c0 == c1) {
                return true;
            }
            
            return false;
        }
        else if (isCapitalLetter(c0) && isLowerCaseLetter(c1)) {
            if (c0 - 'A' == c1 - 'a') {
                return true;
            }
            
            return false;
        }
        else if (isLowerCaseLetter(c0) && isCapitalLetter(c1)) {
            if (c0 - 'a' == c1 - 'A') {
                return true;
            }
            
            return false;
        }
        else {
            return false;
        }
    }
    
    private boolean isValidCharacter(char c) {
        if (isLowerCaseLetter(c) || isCapitalLetter(c) || isNumeric(c)) {
            return true;
        }
        
        return false;
    }
    
    private boolean isCapitalLetter(char c) {
        if (c >= 'A' && c <= 'Z') {
            return true;
        }
        
        return false;
    }
    
    private boolean isLowerCaseLetter(char c) {
        if (c >= 'a' && c <= 'z') {
            return true;
        }
        
        return false;
    }
    
    private boolean isNumeric(char c) {
        if (c >= '0' && c <= '9') {
            return true;
        }
        
        return false;
    }
}
