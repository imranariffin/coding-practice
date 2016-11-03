public class Solution {
    public boolean validWordSquare(List<String> words) {
        for (int i = 0; i < words.size(); i++) {
            String rowString = words.get(i);
            String colString = getColString(words, i);
            
            // System.out.printf("row=%s ? col=%s\n", rowString, colString);
            
            if (!rowString.equals(colString)) {
                return false;
            }
        }
        
        return true;
    }
    
    private String getColString(List<String> words, int col) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < words.size(); i++) {
            if (col < words.get(i).length()) {
                sb.append(words.get(i).charAt(col));
            }
        }
        
        return sb.toString();
    }
}
