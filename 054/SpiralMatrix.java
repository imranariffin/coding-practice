import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ret = new ArrayList<Integer>();

        int n;
        int m = matrix.length;
        if (m == 0)
        	return ret;
        n = matrix[0].length;
        if (n == 1 && m == 1) {
        	ret.add(matrix[0][0]);
        	return ret;
        }

        int cycle = 0;
        int nelements = m*n;
        while (ret.size() < nelements) {
        	if (cycle%2 == 0) {
                // horizontal
        		if (cycle%4 == 0) {
        			// right
                    int h = matrix.length;
                    int w = matrix[0].length;
                    int sj = (cycle>>2);
                    int ej = w - (cycle>>2);
                    int i = (cycle>>2);
                    for (int j = sj; j < ej; j++) {
                        ret.add(matrix[i][j]);
                    }
        		}
        		else {
                    // left
                    int h = matrix.length;
                    int w = matrix[0].length;
                    int sj = w - (cycle>>2) - 2;
                    int ej = (cycle>>2);
                    int i = h - (cycle>>2) - 1;
                    for (int j = sj; j >= ej; j--) {
                        ret.add(matrix[i][j]);
                    }
        		}
        	}
        	else {
                // vertical
        		if (cycle%4 == 1) {
                    // down
                    int h = matrix.length;
                    int w = matrix[0].length;
                    int si = (cycle>>2) + 1;
                    int ei = h - (cycle>>2);
                    int j = w - (cycle>>2) - 1;
                    for (int i = si; i < ei; i++) {
                        ret.add(matrix[i][j]);
                    }
        		}
        		else {
                    // up
                    int h = matrix.length;
                    int w = matrix[0].length;
                    int si = h - (cycle>>2) - 2;
                    int ei = (cycle>>2) + 1;
                    int j = (cycle>>2);
                    for (int i = si; i >= ei; i--) {
                        ret.add(matrix[i][j]);
                    }
        		}
        	}
            cycle++;
        }
        return ret;
    }

    // private void 
    // extendTopPanel(List<Integer> ls, int[][] matrix, int cycle) {
    //     int h = matrix.length;
    //     int w = matrix[0].length;
    //     int sj = (cycle>>2);
    //     int ej = w - (cycle>>2);
    //     int i = (cycle>>2);
    //     for (int j = sj; j < ej; j++) {
    //         ls.add(matrix[i][j]);
    //     }
    // }

    // private void 
    // extendRightPanel(List<Integer> ls, int[][] matrix, int cycle) {
    //     int h = matrix.length;
    //     int w = matrix[0].length;
    //     int si = (cycle>>2) + 1;
    //     int ei = h - (cycle>>2);
    //     int j = w - (cycle>>2) - 1;
    //     for (int i = si; i < ei; i++) {
    //         ls.add(matrix[i][j]);
    //     }
    // }

    // private void 
    // extendBottomPanel(List<Integer> ls, int[][] matrix, int cycle) {
    //     int h = matrix.length;
    //     int w = matrix[0].length;
    //     int sj = w - (cycle>>2) - 2;
    //     int ej = (cycle>>2);
    //     int i = h - (cycle>>2) - 1;
    //     for (int j = sj; j >= ej; j--) {
    //         ls.add(matrix[i][j]);
    //     }
    // }

    // private void 
    // extendLeftPanel(List<Integer> ls, int[][] matrix, int cycle) {
    //     int h = matrix.length;
    //     int w = matrix[0].length;
    //     int si = h - (cycle>>2) - 2;
    //     int ei = (cycle>>2) + 1;
    //     int j = (cycle>>2);
    //     for (int i = si; i >= ei; i--) {
    //         ls.add(matrix[i][j]);
    //     }
    // }

    public static void main(String[] args) {
    	SpiralMatrix sm = new SpiralMatrix();

    	int[][] matrix = {
    		{1, 2, 3, 4},
    		{5, 6, 7, 8},
    		{9, 10, 11, 12},
    		{13, 14, 15, 16},
    	};
    	// print matrix normally
    	sm.printMatrix(matrix);
        // print spiral
    	System.out.println(sm.spiralOrder(matrix));

        int[][] matrix2 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12},
        };
        // print matrix normally
        sm.printMatrix(matrix2);
        // print spiral
        System.out.println(sm.spiralOrder(matrix2));

    	return;
    }

    private void printMatrix(int[][] matrix) {
        int h = matrix.length;
        int w = matrix[0].length;
    	for (int i = 0; i < h; i++) {
    		for (int j = 0; j < w; j++) {
    			System.out.print(matrix[i][j] + " ");
    		}
    		System.out.print("\n");
    	}
    }
}