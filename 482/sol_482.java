public class Solution {
    public String licenseKeyFormatting(String S, int K) {
        String s = S.replaceAll("-", "").toUpperCase();
        StringBuilder sb = new StringBuilder();
        int c = 0;
        char[] carr = s.toCharArray();
        for (int i = carr.length - 1; i >= 0; --i) {
            if (c >= K) {
                sb.append("-");
                c = 0;
            }
            sb.append(carr[i]);
            c += 1;
        }
        return sb.reverse().toString();
    }
}
