public class Solution {
    public String longestPalindrome(String s) {
        
        // Trivial case
        if (s.length() < 2) {
            return s;
        }
        
        // Where [start, end] = palindrome
        int start = 0;
        int end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int longer = Math.max(expandAroundCenter(s, i, i), expandAroundCenter(s, i, i + 1));
            
            if (longer > end - start + 1) {
                
                // For even case, index i is the first left index after the center.
                // So, the left length needs to be cut by 1 element.
                // Length is cut before the division since cutting it afterwards will affect
                // odd length behavior.
                // Odd length behavior is correct since index i represents the center index
                // and integer division is rounded down.
                start = i - (longer - 1) / 2;
                end = i + longer / 2;
            }
        }
        
        return s.substring(start, end + 1);
    }
    
    private int expandAroundCenter(String s, int i, int j) {
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        
        // Need to trim the numbers down since the while loop will always offshoot
        // by 1 since it can't predict the future!
        return (--j - ++i) + 1;
    }
}
