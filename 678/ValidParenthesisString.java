class Solution {
    public boolean checkValidString(String str) {
        return check(str, 0, 0);
    }
    
    private boolean check(String str, int start, int count) {
        if (count < 0) {
            return false;
        }
        
        for (int i = start; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(') {
                count++;
            } else if (c == ')') {
                if (count <= 0) {
                    return false;
                }
                count--;
            } else if (c == '*') {
                return (
                    check(str, i + 1, count)
                    || check(str, i + 1, count - 1)
                    || check(str, i + 1, count + 1)
                );
            }
        }
        return count == 0;
    }
}
