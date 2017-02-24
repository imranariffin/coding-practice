public class Solution {
	public String reverseString(String s) {
		StringBuilder sb = new StringBuilder();

		char[] cArr = s.toCharArray();
		for (int i=cArr.length-1; i>=0; i--) {
			char c = cArr[i];
			sb.append(c);
		}
		return sb.toString();
	}

	public static void
	main(String[] args) {
		Solution s = new Solution();

		System.out.println(s.reverseString("abcdefgh"));

		return;
	}
}