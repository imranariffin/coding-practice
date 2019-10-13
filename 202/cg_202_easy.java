public class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> S = new HashSet<Integer>();
        
        while (n != 1) {
            int sqSum = 0;
            
            while (n != 0) {
                sqSum += (n % 10) * (n % 10);
                n /= 10;
            }
            
            // System.out.println(sqSum);
            
            if (S.contains(sqSum)) {
                return false;
            }
            
            S.add(sqSum);
            n = sqSum;
        }
        
        return true;
    }
}
