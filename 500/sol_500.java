public class Solution {
    public String[] findWords(String[] words) {
        List<String> res = new LinkedList<>();

        for (String word : words) {
            String word_lower = word.toLowerCase();
            Set<Integer> set = new HashSet<>();

            for (int j = 0; j < word_lower.length(); ++j) {
                char ch = word_lower.charAt(j);
                set.add(charRow(ch));
            }

            if (set.size() == 1) {
                res.add(word);
            }
        }

        String[] res_arr = new String[res.size()];

        for (int i = 0; i < res.size(); ++i) {
            res_arr[i] = res.get(i);
        }

        return res_arr;
    }

    private int charRow(char ch) {
        switch (ch) {
            case 'q':
            case 'w':
            case 'e':
            case 'r':
            case 't':
            case 'y':
            case 'u':
            case 'i':
            case 'o':
            case 'p':
                return 0;
            case 'a':
            case 's':
            case 'd':
            case 'f':
            case 'g':
            case 'h':
            case 'j':
            case 'k':
            case 'l':
                return 1;
            case 'z':
            case 'x':
            case 'c':
            case 'v':
            case 'b':
            case 'n':
            case 'm':
                return 2;
            default:
                return -1;
        }
    }
}
