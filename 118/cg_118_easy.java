public class Solution {
    public List<List<Integer>> generate(int numRows) {
        int row = 0;
        List<List<Integer>> res = new ArrayList<>();
        
        while (row < numRows) {
            if (row == 0) {
                res.add(new ArrayList<Integer>());
                res.get(row).add(1);
                row++;
                
                continue;
            }
            
            res.add(new ArrayList<Integer>());
            res.get(row).add(1);
            
            for (int i = 1; i < res.get(row - 1).size(); i++) {
                res.get(row).add(res.get(row - 1).get(i) + res.get(row - 1).get(i - 1));
            }
            
            res.get(row).add(1);
            row++;
        }
        
        return res;
    }
}
