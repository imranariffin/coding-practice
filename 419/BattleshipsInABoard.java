class Solution {
    Set<String> visited = new HashSet<>();
    
    public int countBattleships(char[][] board) {
        if (board == null) {
            return 0;
        }
        int h = board.length;
        int w = board[0].length;
        
        int ret = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (!visited.contains(i + "," + j) && board[i][j] == 'X') {
                    dfs(board, i, j, null);
                    ret++;
                }
            }
        }
        
        return ret;
    }
    
    private void dfs(char[][] board, int i, int j, String dir) {
        if (visited.contains(i + "," + j) 
            || i < 0 || i >= board.length
            || j < 0 || j >= board[0].length
            || board[i][j] == '.' 
           ) {
            return;
        }
        visited.add(i + "," + j);
        
        if (dir == "HORIZONTAL") {
            dfs(board, i, j + 1, "HORIZONTAL");
            dfs(board, i, j - 1, "HORIZONTAL");
        } else if (dir == "VERTICAL") {
            dfs(board, i + 1, j, "VERTICAL");
            dfs(board, i - 1, j, "VERTICAL");   
        } else {
            dfs(board, i, j + 1, "HORIZONTAL");
            dfs(board, i, j - 1, "HORIZONTAL");
            dfs(board, i + 1, j, "VERTICAL");
            dfs(board, i - 1, j, "VERTICAL");
        }
        return;
    }
}
