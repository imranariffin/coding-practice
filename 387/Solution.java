class Solution {
    public int firstUniqChar(String s) {
        int[] counter = new int[26];
        char[] chars = s.toCharArray();
        for (char c: chars) {
            counter[c - 'a']++;
        }
        for (int i = 0; i < chars.length; i++) {
            char c = chars[i];
            if (counter[c - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
