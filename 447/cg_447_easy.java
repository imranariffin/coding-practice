public class Solution {
    public int numberOfBoomerangs(int[][] points) {
        HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
        int res = 0;
        
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                }
                
                int distance = getDistance(points[i], points[j]);
                
                m.put(distance, m.getOrDefault(distance, 0) + 1);
            }
            
            for (int val : m.values()) {
                res += val * (val - 1);
            }
            
            m.clear();
        }
        
        return res;
    }
    
    private int getDistance(int[] a, int[] b) {
        int xAB = a[0] - b[0];
        int yAB = a[1] - b[1];
        
        xAB *= xAB;
        yAB *= yAB;
        
        return xAB + yAB;
    }
}
