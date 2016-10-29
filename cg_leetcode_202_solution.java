public class Solution {
    public boolean isHappy(int n) {
        int loop = 0;
        
        while (loop < 1000) {
            n = calculate(toIntList(n));
            
            if (n == 1) {
                return true;
            }
            
            loop += 1;
        }
        
        return false;
    }
    
    private ArrayList<Integer> toIntList(int x) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        
        String s = Integer.toString(x);
        
        for (int i = 0; i < s.length(); i++) {
            res.add(s.charAt(i) - '0');
        }
        
        return res;
    }
    
    private int calculate(ArrayList<Integer> arrList) {
        int res = 0;
        
        Iterator<Integer> it = arrList.iterator();
        
        while (it.hasNext()) {
            int x = it.next();
            
            res += x * x;
        }
        
        return res;
    }
}