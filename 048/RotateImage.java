/*
	Rotate nxn matrix in-place 90-degree CW
*/

import java.util.Arrays;

public class RotateImage {
	public static int[][] rotate(int[][] matrix) {
		if (matrix == null || matrix.length == 0) {
			return matrix;
		}

		int radius = matrix.length%2==0? matrix.length/2: matrix.length/2+1;
		for (int r=0; r<radius; r++) {
			_rotate_(matrix, r);
		}
		return matrix;
	}

	private static void _rotate_(int[][] matrix, int r) {
		boolean even = matrix.length%2==0? true:false;
		int len = even? r*2+1:r*2;
		int w = matrix.length;
		int temp; 
		int i_right, j_right, i_top, j_top, i_left, j_left, i_bottom, j_bottom;
		for (int k=0; k<len; k++) {
			// positions of right, top, left & bottom panels
			if (even) {
				i_right = w/2 - 1 - r + k;
				j_right = w/2 + r;
				i_top = w/2 - r - 1;
				j_top = w/2 - 1 - r + k;
				i_left = w/2 + r - k;
				j_left = w/2 - r - 1;
				i_bottom = w/2 + r;
				j_bottom = w/2 + r - k;				
			} else {
				i_right = w/2 - r + k;
				j_right = w/2 + r;
				i_top = w/2 - r;
				j_top = w/2 - r + k;
				i_left = w/2 + r - k;
				j_left = w/2 - r;
				i_bottom = w/2 + r;
				j_bottom = w/2 + r - k;
			}

			// swap
			temp = matrix[i_right][j_right];
			matrix[i_right][j_right] = matrix[i_top][j_top];
			matrix[i_top][j_top] = matrix[i_left][j_left];
			matrix[i_left][j_left] = matrix[i_bottom][j_bottom];
			matrix[i_bottom][j_bottom] = temp;
		}
	}

	private static void printMatrix(int[][] matrix) {
		System.out.println("-------------");
		for (int[] row: matrix) {
			System.out.println(Arrays.toString(row));
		}
		System.out.println("-------------");
	}

	public static void main(String[] args) {
		int[][] image = {
			{4,4,4,1},
			{3,4,1,1},
			{3,3,2,1},
			{3,2,2,2}
		};
		printMatrix(image);
		image = rotate(image);
		printMatrix(image);

		int[][] image2 = {
			{4,4,1},
			{3,0,1},
			{3,2,2}
		};
		printMatrix(image2);
		image2 = rotate(image2);
		printMatrix(image2);
	}
}