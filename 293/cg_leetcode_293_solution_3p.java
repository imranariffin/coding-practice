public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        ArrayList<String> res = new ArrayList<String>();
        
        for (int i = 0; i < s.length() - 1; i++) {
            Character c1 = s.charAt(i);
            Character c2 = s.charAt(i + 1);
            
            if (c1 == '+' && c2 == '+') {
                res.add(s.substring(0, i) + "--" + s.substring(i + 2));
            }
        }
        
        return res;
    }
}
