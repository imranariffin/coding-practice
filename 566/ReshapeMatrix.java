public class ReshapeMatrix {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int m = nums.length, n = nums[0].length;
        int size = n*m, sizeNew = r*c;
        if (size != sizeNew) {
            return nums;
        }
        
        List<Integer> ls = new ArrayList<Integer>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ls.add(nums[i][j]);
            }
        }
        
        int[][] ret = new int[r][c];
        for (int i = 0; i < sizeNew; i++) {
            ret[i/c][i%c] = ls.get(i);
        }
        
        return ret;
    }
}