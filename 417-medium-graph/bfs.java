public class Solution {
    int[][] flows = new int[][] {{1,0},{-1,0},{0,1},{0,-1}};

    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> result = new LinkedList<>();

        int m = matrix.length;
        int n = m != 0 ? matrix[0].length : 0;

        boolean[][] visitedPacific = new boolean[m][n];
        boolean[][] visitedAtlantic = new boolean[m][n];

        Queue<Vertex> queuePacific = new LinkedList<>();
        Queue<Vertex> queueAtlantic = new LinkedList<>();

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (row == 0 || col == 0) {
                    visitedPacific[row][col] = true;
                    queuePacific.offer(new Vertex(row, col));
                }

                if (row == m - 1 || col == n - 1) {
                    visitedAtlantic[row][col] = true;
                    queueAtlantic.offer(new Vertex(row, col));
                }
            }
        }

        bfs(matrix, visitedPacific, queuePacific);
        bfs(matrix, visitedAtlantic, queueAtlantic);

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (visitedPacific[row][col] && visitedAtlantic[row][col]) {
                    result.add(new int[] {row,col});
                }
            }
        }

        return result;
    }

    private void bfs(int[][] matrix, boolean[][] visited, Queue<Vertex> q) {
        int m = matrix.length;
        int n = m != 0 ? matrix[0].length : 0;

        while (!q.isEmpty()) {
            Vertex u = q.poll();

            for (int[] flow : flows) {
                Vertex v = new Vertex(u.row + flow[0], u.col + flow[1]);

                if (v.row < 0 || v.row >= m || v.col < 0 || v.col >= n) {
                    continue;
                }

                if (!visited[v.row][v.col] && isFlowFromTo(matrix, v, u)) {
                    visited[v.row][v.col] = true;
                    q.offer(v);
                }
            }
        }
    }

    private boolean isFlowFromTo(int[][] matrix, Vertex u, Vertex v) {
        return matrix[u.row][u.col] >= matrix[v.row][v.col] ? true : false;
    }

    public class Vertex {
        public int row;
        public int col;

        public Vertex(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}
