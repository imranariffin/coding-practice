public class Solution {
    public int hammingDistance(int x, int y) {
        int c = 0;
        int z = x ^ y;
        String zSt = Integer.toBinaryString(z);

        for (int i = 0; i < zSt.length(); i++) {
            if (zSt.charAt(i) == '1') {
                c++;
            }
        }

        return c;
    }
}
