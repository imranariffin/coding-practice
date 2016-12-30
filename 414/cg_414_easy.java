public class Solution {
    public int thirdMax(int[] nums) {
        if (nums.length < 1) {
            return 0;
        }
        
        int[] tableMax3 = new int[3];
        boolean[] tableMax3Valid = new boolean[tableMax3.length];
        
        for (int num : nums) {
            updateMaxTable(tableMax3, tableMax3Valid, num);
        }
        
        if (!tableMax3Valid[0]) {
            return tableMax3[tableMax3.length - 1];
        }
        
        return tableMax3[0];
    }
    
    private void updateMaxTable(int[] table, boolean[] occupied, int maxCandidate) {
        int i = table.length - 1;
        
        while (i >= 0) {
            if (!occupied[i]) {
                table[i] = maxCandidate;
                occupied[i] = true;
                
                break;
            }
            if (table[i] == maxCandidate) {
                break;
            }
            else if (table[i] < maxCandidate) {
                for (int j = 0; j < i; j++) {
                    table[j] = table[j + 1];
                    occupied[j] = occupied[j + 1];
                }
                
                table[i] = maxCandidate;
                occupied[i] = true;
                
                break;
            }
            else {
            }
            
            i--;
        }
    }
    
    private String getTablePrint(int[] table) {
        if (table.length < 1) {
            return "";
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (int val : table) {
            sb.append(val);
            sb.append(", ");
        }
        
        return sb.toString().substring(0, sb.toString().length() - 2);
    }
}
