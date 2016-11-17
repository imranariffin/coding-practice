public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        
        res.add(1);
        
        for (int i = 1; i <= rowIndex; i++) {
            res.add(0, 1);
            
            for (int j = 2; j < res.size(); j++) {
                int num = res.get(j - 1) + res.get(j);
                
                res.set(j - 1, num);
            }
        }
        
        return res;
    }
}
