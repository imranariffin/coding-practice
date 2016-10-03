import java.util.ArrayList;

public class StrStr {
	public int strStr(String haystack, String needle) {
		// special cases
		if (haystack.equals("") && needle.equals("")) return 0;
		if (haystack.equals("")) return -1;
		if (needle.equals("")) return 0;


		int l = needle.length();
		ArrayList<String> queue = new ArrayList<String>();

		// seed needle
		// char needleArr[] = needle.toCharArray();
		for (int i=0; i<l-1; i++) {
			queue.add(String.valueOf(needle.charAt(i)));
		}

		// find needle
		int ll = haystack.length();
		for (int i=0; i<ll-l+1; i++) {
			// shift
			queue.add(String.valueOf(haystack.charAt(i+l-1)));

			// compare
			String ss = haystack.substring(i, i+l);
			System.out.println(ss);
			boolean same = true;
			for (int j=0; j<l; j++) {
				if (ss.charAt(j) != needle.charAt(j)) {
					same = false;
					break;
				}
			}
			if (same)
				return i;

			// shift
			queue.remove(0);
		}
		return -1;
	}

	public static void
	main(String[] args) {
		if (args.length < 2) return;

		String haystack = args[0];
		String needle = args[1];

		StrStr sStr = new StrStr();
		System.out.println(sStr.strStr(haystack, needle));
	}
}