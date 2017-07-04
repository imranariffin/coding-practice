import java.util.Arrays;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0|| matrix[0].length == 0) {
            return false;
        }

        int j = matrix[0].length-1;
        int height = matrix.length;
        int i = 0;

        int e;
        while (i < height && j >= 0) {
        	e = matrix[i][j];
        	if (e == target) {
        		return true;
        	} else if (target < matrix[i][j]) {
        		j--;
        	} else {
        		i++;
        	}
        }
        return false;
    }

    public static void main(String[] args) {
    	Solution s = new Solution();

    	System.out.println("TEST 0");
    	int[][] matrix0 = {
    		{1, 2},
    		{3, 4}
    	};
    	int target0 = 3;
    	s.printMatrix(matrix0);
    	System.out.println(target0);
    	System.out.println(s.searchMatrix(matrix0, target0));

    	System.out.println("TEST 1");
    	int[][] matrix1 = {
    		{1, 2},
    		{3, 4}
    	};
    	int target1 = 5;
    	s.printMatrix(matrix1);
    	System.out.println(target1);
    	System.out.println(s.searchMatrix(matrix1, target1));
    }

    private void printMatrix(int[][] matrix) {
    	for(int[] row: matrix) {
    		System.out.println(Arrays.toString(row));
    	}
    }
}