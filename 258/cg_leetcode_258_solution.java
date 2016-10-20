public class Solution {
    public int addDigits(int num) {
        int res = num;
        
        while (res > 9) {
            res = add(getDigits(res));
        }
        
        return res;
    }
    
    private int convert(char c) {
        return (c >= '0' && c <= '9') ? c - '0' : -1;
    }
    
    private ArrayList<Integer> getDigits(int num) {
        String str = Integer.toString(num);
        
        ArrayList<Integer> res = new ArrayList<Integer>();
        
        for (int i = 0; i < str.length(); i++) {
            res.add(convert(str.charAt(i)));
        }
        
        return res;
    }
    
    private int add(ArrayList<Integer> arr) {
        int res = 0;
        
        for (int i = 0; i < arr.size(); i++) {
            res += arr.get(i);
        }
        
        return res;
    }
}
