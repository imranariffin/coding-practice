public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        if (A.length < 3) {
            return 0;
        }
        
        int lf = 0;
        int rg = 1;
        int sliceCount = 0;
        
        while (lf < A.length && rg + 1 < A.length) {
            if (A[rg + 1] - A[rg] == A[rg] - A[rg - 1]) {
                rg++;
            }
            else {
                // System.out.printf("section: [%d,%d] = ", lf, rg);
                // System.out.printf("%d\n", countInnerSlice(A, lf, rg));
                sliceCount += countInnerSlice(A, lf, rg);
                
                lf = rg;
                rg = lf + 1;
            }
        }
        
        // System.out.printf("section: [%d,%d] = ", lf, rg);
        // System.out.printf("%d\n", countInnerSlice(A, lf, rg));
        sliceCount += countInnerSlice(A, lf, rg);
        
        return sliceCount;
    }
    
    private int countInnerSlice(int[] A, int lf, int rg) {
        if (rg - lf < 2) {
            return 0;
        }
        
        int sliceCount = 0;
        int p = rg;
        
        while (p - lf > 1) {
            sliceCount += rg - p + 1;
            p--;
        }
        
        return sliceCount;
    }
}
