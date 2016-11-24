public class Solution {
    public int islandPerimeter(int[][] grid) {
        int beach = 0;

        int[][] moves = {
            {  0,  1 },
            {  1,  0 },
            {  0, -1 },
            { -1,  0 }
        };

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    for (int[] move : moves) {
                        int ni = i + move[0];
                        int nj = j + move[1];
                        if (ni >= 0 && ni < grid.length && nj >= 0 && nj < grid[ni].length) {
                            beach += grid[ni][nj] == 0 ? 1 : 0;
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
