public class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int row = 0; row < 9; row++) {
            if (!checkRow(board, row)) {
                return false;
            }
        }
        
        for (int col = 0; col < 9; col++) {
            if (!checkCol(board, col)) {
                return false;
            }
        }
        
        for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {
                if (!checkBlock(board, row, col)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean checkRow(char[][] board, int row) {
        Set<Character> S = new HashSet<>();
        
        for (int col = 0; col < 9; col++) {
            if (board[row][col] != '.' && S.contains(board[row][col])) {
                return false;
            }
            
            S.add(board[row][col]);
        }
        
        return true;
    }
    
    private boolean checkCol(char[][] board, int col) {
        Set<Character> S = new HashSet<>();
        
        for (int row = 0; row < 9; row++) {
            if (board[row][col] != '.' && S.contains(board[row][col])) {
                return false;
            }
            
            S.add(board[row][col]);
        }
        
        return true;
    }
    
    private boolean checkBlock(char[][] board, int row, int col) {
        Set<Character> S = new HashSet<>();
        
        for (int r = row; r < row + 3; r++) {
            for (int c = col; c < col + 3; c++) {
                if (board[r][c] != '.' && S.contains(board[r][c])) {
                    return false;
                }
                
                S.add(board[r][c]);
            }
        }
        
        return true;
    }
}
