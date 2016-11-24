public class Solution {
    public int islandPerimeter(int[][] grid) {
        int beach = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int[][] moves = {
                    { i, j + 1 },
                    { i + 1, j },
                    { i, j - 1 },
                    { i - 1, j }
                };
                
                if (grid[i][j] == 1) {
                    for (int[] move : moves) {
                        if (move[0] >= 0 && move[0] < grid.length && move[1] >= 0 && move[1] < grid[move[0]].length) {
                            beach += grid[move[0]][move[1]] == 0 ? 1 : 0;
                        }
                        else {
                            beach += 1;
                        }
                    }
                }
            }
        }
        
        return beach;
    }
}
