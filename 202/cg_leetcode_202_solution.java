public class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> S = new HashSet<Integer>();
        
        while (n != 1) {
            if (!S.contains(n)) {
                S.add(n);
            }
            else {
                return false;
            }
            
            int add = 0;
            
            while (n != 0) {
                add += (n % 10) * (n % 10);
                n /= 10;
            }
            
            n = add;
        }
        
        return true;
    }
}
