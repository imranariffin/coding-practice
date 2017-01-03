public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (c1, c2) -> -(c1[0] - c2[0]) * (Math.abs(c1[1] - c2[1]) + 1) + (c1[1] - c2[1]));
        
        // System.out.print("Sort: ");
        // printArr(people);
        
        int[][] res = new int[people.length][2];
        boolean[] occ = new boolean[res.length];
        
        for (int i = 0; i < people.length; i++) {
            int bCount = 0;
            
            for (int j = 0; j < res.length; j++) {
                if (!occ[j]) {
                    res[j][0] = people[i][0];
                    res[j][1] = people[i][1];
                    occ[j] = true;
                    
                    break;
                }
                
                if (bCount >= people[i][1]) {
                    for (int k = res.length - 1; k > j; k--) {
                        res[k][0] = res[k - 1][0];
                        res[k][1] = res[k - 1][1];
                        occ[k] = occ[k - 1];
                    }
                    
                    res[j][0] = people[i][0];
                    res[j][1] = people[i][1];
                    
                    break;
                }
                
                bCount += res[j][0] >= people[i][0] ? 1 : 0;
            }
            
            // System.out.printf("Insert [%d,%d]: ", people[i][0], people[i][1]);
            // printArr(res);
        }
        
        return res;
    }
    
    private void printArr(int[][] people) {
        for (int i = 0; i < people.length; i++) {
            System.out.printf("[%d,%d] ", people[i][0], people[i][1]);
        }
        
        System.out.println();
    }
}
