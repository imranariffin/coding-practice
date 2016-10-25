public class Solution {
    public List<String> readBinaryWatch(int num) {
        ArrayList<String> res = new ArrayList<String>();
        
        for (int hr = 0; hr < 12; hr++) {
            for (int mn = 0; mn < 60; mn++) {
                String hrStr = Integer.toBinaryString(hr);
                String mnStr = Integer.toBinaryString(mn);
                
                if (count1s(hrStr) + count1s(mnStr) == num) {
                    res.add(Integer.toString(hr) + ":" + getProperMin(mn));
                }
            }
        }
        
        return res;
    }
    
    private int count1s(String s) {
        int res = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                res++;
            }
        }
        
        return res;
    }
    
    private String getProperMin(int min) {
        if (min < 0) {
            return "-1";
        }
        
        if (min < 10) {
            return "0" + Integer.toString(min);
        }
        
        return Integer.toString(min);
    }
}
