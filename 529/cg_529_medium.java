public class Solution {
    int[][] adjs = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 } };

    public char[][] updateBoard(char[][] board, int[] click) {
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';

            return board;
        }

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(click);

        while (!queue.isEmpty()) {
            int[] u = queue.poll();
            int mineCount = 0;

            for (int[] adj : adjs) {
                int[] v = { u[0] + adj[0], u[1] + adj[1] };

                if (v[0] < 0 || v[0] >= board.length || v[1] < 0 || v[1] >= board[0].length) {
                    continue;
                }

                if (board[v[0]][v[1]] == 'M') {
                    mineCount += 1;
                }
            }

            if (mineCount > 0) {
                board[u[0]][u[1]] = (char)(mineCount + '0');

                continue;
            }

            for (int[] adj : adjs) {
                int[] v = { u[0] + adj[0], u[1] + adj[1] };

                if (v[0] < 0 || v[0] >= board.length || v[1] < 0 || v[1] >= board[0].length) {
                    continue;
                }

                if (board[v[0]][v[1]] == 'E') {
                    queue.offer(v);

                    // Mark visited vertex so we don't choose it again later. This is to prevent
                    // out of memory error.
                    board[v[0]][v[1]] = 'V';
                }
            }

            board[u[0]][u[1]] = 'B';
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'V') {
                    board[i][j] = 'B';
                }
            }
        }

        return board;
    }
}
