public class StrStr {
	public static int strStr(String haystack, String needle) {
		return haystack.indexOf(needle);
	}

	public static void
	main(String[] args) {
		String haystack = "";
		String needle = "";
		String printStr = "haystack=%s, needle=%s\nAns: %s\nExpected: %s\n";
		String ans = "0";
		System.out.format(
			printStr, 
			haystack, 
			needle, 
			strStr(haystack, needle),
			ans);

		haystack = "ab";
		needle = "b";
		printStr = "haystack=%s, needle=%s\nAns: %s\nExpected: %s\n";
		ans = "1";
		System.out.format(
			printStr, 
			haystack, 
			needle, 
			strStr(haystack, needle),
			ans);

		haystack = "ab";
		needle = "c";
		printStr = "haystack=%s, needle=%s\nAns: %s\nExpected: %s\n";
		ans = "-1";
		System.out.format(
			printStr, 
			haystack, 
			needle, 
			strStr(haystack, needle),
			ans);		
	}
}