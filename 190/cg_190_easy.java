public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        int m = 1 << 31;
        int tmp = n;

        while (tmp != 0) {
            int x = tmp & 1;

            if (x != 0) {
                res = res | m;
            }

            tmp = tmp >>> 1;
            m = m >>> 1;
        }

        return res;
    }
}
