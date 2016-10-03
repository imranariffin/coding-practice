import java.util.HashMap;

class LongestPalindrome {
	// 23 ms
	HashMap<Character, Integer> counter;

	public int longestPalindrome(String s) {
		int ret = 0;

		counter = new HashMap<Character, Integer>();

		// count char occurences
		for (Character c: s.toCharArray()) {
			if (counter.containsKey(c))
				counter.put(c, counter.get(c)+1);
			else 
				counter.put(c, 1);
		}

		// count even and odd chars
		int n_odd = 0;
		for (Character c: counter.keySet()) {
			int f = counter.get(c);
			if (f%2 == 0)
				ret += f;
			else {
				ret += f-1;
				n_odd += 1;
			}
		}

		// find max odd chars
		int max_f = 0;
		char max_char;
		for (Character c: counter.keySet()) {
			int f = counter.get(c);
			if (f%2 == 1)
				if (f > max_f) {
					max_f = f;
					max_char = c;
				}
		}

		if (n_odd > 0)
			ret += 1;
		return ret;
		}
	}