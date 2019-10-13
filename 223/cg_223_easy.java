public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        return Math.toIntExact(area(A, B, C, D) + area(E, F, G, H) - intersectArea(A, B, C, D, E, F, G, H));
    }
    
    private long intersectArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        long w = (long) Math.min(C, G) - (long) Math.max(A, E);
        long h = (long) Math.min(D, H) - (long) Math.max(B, F);
        
        if (w <= 0 || h <= 0) {
            return 0;
        }
        
        return w * h;
    }
    
    private long area(int A, int B, int C, int D) {
        return ((long) C - (long) A) * ((long) D - (long) B);
    }
}
