public class Solution {
    public int countBattleships(char[][] board) {
        int H = board.length;
        int W = board.length > 0 ? board[0].length : 0;
        int ship = 0;
        int[][] explore = new int[][] { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
        boolean[][] M = new boolean[H][W];
        
        for (int r = 0; r < H; r++) {
            for (int c = 0; c < W; c++) {
                if (board[r][c] == 'X' && !M[r][c]) {
                    ArrayDeque<int[]> D = new ArrayDeque<int[]>();
                    
                    ship += 1;
                    D.offer(new int[] { r, c });
                    
                    while (!D.isEmpty()) {
                        int[] rc = D.poll();
                        
                        M[rc[0]][rc[1]] = true;
                        
                        for (int[] mv : explore) {
                            int rn = rc[0] + mv[0];
                            int cn = rc[1] + mv[1];
                            
                            if (rn >= 0 && rn < H && cn >= 0 && cn < W && board[rn][cn] == 'X' && !M[rn][cn]) {
                                D.offer(new int[] { rn, cn });
                                M[rn][cn] = true;
                            }
                        }
                    }
                }
            }
        }
        
        return ship;
    }
}
