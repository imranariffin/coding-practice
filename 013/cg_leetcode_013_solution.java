public class Solution {
    public int romanToInt(String s) {
        int res = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && singleConvert(s.charAt(i)) < singleConvert(s.charAt(i + 1))) {
                res += singleConvert(s.charAt(i + 1)) - singleConvert(s.charAt(i));
                i++;
                
                continue;
            }
            
            res += singleConvert(s.charAt(i));
        }
        
        return res;
    }
    
    private int singleConvert(char romanChar) {
        switch (romanChar) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return -1;
        }
    }
}
