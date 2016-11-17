public class Solution {
    public int trailingZeroes(int n) {
        /**
         * Refer "https://discuss.leetcode.com/topic/6516/my-one-line-solutions-in-3-languages".
         * 
         * Consider 100! = 100 * 99 * .. * 75 * .. * 25 * .. * 5 * .. * 1.
         * 
         * 100 / 5 = 20, 20 / 5 = 4, and 4 / 5 = 0.
         * 
         * 100 / 5 = 20 (5, 10, 15, 20, .. , 100).  <-- OK.
         * 20 / 5 = 4 (5, 10, 15, 20).  <-- Why?
         * 4 / 5 = 0 ().  <-- Why?
         * 
         * The reason we are interested in number 5 is because a trailing zero is produced when we multiply a multiple of 5
         * with an even number. Since even numbers are plentiful in 100!, we just assume we will have enough
         * of them to pair up with our multiple of 5s.
         */
        return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);
    }
}
