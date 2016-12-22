public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length < 1) {
            return "";
        }

        int smallestIndex = 0;
        int smallestLength = strs[smallestIndex].length();

        for (int i = 0; i < strs.length; i++) {
            if (strs[i].length() < smallestLength) {
                smallestIndex = i;
                smallestLength = strs[i].length();
            }
        }

        String prefix = strs[smallestIndex];

        while (prefix.length() > 0) {
            boolean ok = true;

            for (String s : strs) {
                if (prefix.compareTo(s.substring(0, prefix.length())) != 0) {
                    ok = false;
                }
            }

            if (ok) {
                return prefix;
            }

            prefix = prefix.substring(0, prefix.length() - 1);
        }

        return "";
    }
}
