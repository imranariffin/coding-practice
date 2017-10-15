import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class PascalTriangle {

	public List<Integer> getRow(int rowIndex) {
		if (rowIndex == 0) {
			Integer[] ret = {1};
			return Arrays.asList(ret);
		}
		if (rowIndex == 1) {
			Integer[] ret = {1, 1};
			return Arrays.asList(ret);
		}

		Integer[] ret = new Integer[2], temp;
		ret[0] = 1; ret[1] = 1;

		for (int r = 0; r <= rowIndex; r++) {
			temp = new Integer[r + 1];
			temp[0] = 1; temp[r] = 1;
			for (int c = 1; c < r; c++) {
				Integer pre = ret[c - 1];
				Integer post = ret[c];
				temp[c] = pre + post;
			}
			ret = temp;
		}

		return Arrays.asList(ret);
	}

	public static void main(String[] args) {
		PascalTriangle pt = new PascalTriangle();


		int N = 21;
		for (int n = 0; n <= N; n++) {
			System.out.format("%s: %s\n", n, pt.getRow(n));
		}
		System.out.format("%s: %s\n", N, pt.getRow(N));
	}
}