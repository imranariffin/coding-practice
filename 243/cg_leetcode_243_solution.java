public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        HashMap<String, ArrayList<Integer>> m = new HashMap<String, ArrayList<Integer>>();
        
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            
            if (m.containsKey(word)) {
                m.get(word).add(i);
            }
            else {
                m.put(word, new ArrayList<Integer>());
                m.get(word).add(i);
            }
        }
        
        int res = Integer.MAX_VALUE;
        
        for (int i = 0; i < m.get(word1).size(); i++) {
            for (int j = 0; j < m.get(word2).size(); j++) {
                res = Math.min(res, Math.abs(m.get(word1).get(i) - m.get(word2).get(j)));
            }
        }
        
        return res;
    }
}
