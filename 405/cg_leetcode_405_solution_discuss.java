public class Solution {
    char[] T = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };
    
    public String toHex(int num) {
        if (num == 0) {
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        
        while (num != 0) {
            sb.append(T[(num & 15)]);
            num = num >>> 4;
        }
        
        return sb.reverse().toString();
    }
}
