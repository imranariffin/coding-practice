public class Solution {
    public int[] countBits(int num) {
        int[] res = new int[num + 1];
        
        for (int i = 0; i <= num; i++) {
            int x = i;
            
            res[i] = calculate(x);
        }
        
        return res;
    }
    
    private int calculate(int x) {
        int count = 0;
        
        while (x != 0) {
            count += x & 1;
            x = x >>> 1;
        }
        
        return count;
    }
}
