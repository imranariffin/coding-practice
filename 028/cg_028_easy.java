public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) {
            return 0;
        }

        for (int i = 0; i < haystack.length(); i++) {
            if (i + needle.length() > haystack.length()) {
                break;
            }

            if (haystack.substring(i, i + needle.length()).compareTo(needle) == 0) {
                return i;
            }
        }

        return -1;
    }
}
