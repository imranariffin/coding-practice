public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int cookie = 0;
        int child = 0;
        int satisfy = 0;
        
        while (cookie < s.length && child < g.length) {
            if (s[cookie] >= g[child]) {
                cookie++;
                child++;
                satisfy++;
            }
            else {
                cookie++;
            }
        }
        
        return satisfy;
    }
}
