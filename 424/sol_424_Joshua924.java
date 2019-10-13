public class Solution {

    public int characterReplacement(String s, int k) {
        int n = s.length();

        // Sliding window (sw).
        int start = 0;
        int end = 0;

        // Character count to keep track of sw characters.
        int[] chCount = new int[26];

        // Majority character count. If x is majority character, characters
        // other than x will consume k.
        int majorCC = 0;

        // sw maximum length.
        int maxLen = 0;

        while (end < n) {
            majorCC = Math.max(majorCC, ++chCount[s.charAt(end) - 'A']);

            // (end - start + 1) == length of sw. The while loop can be replaced with
            // an if statement since chCount only increments by 1 in each loop.
            while ((end - start + 1) - majorCC > k) {
                --chCount[s.charAt(start) - 'A'];
                ++start;
            }

            maxLen = Math.max(maxLen, (end - start + 1));
            end++;
        }

        return maxLen;
    }
}
