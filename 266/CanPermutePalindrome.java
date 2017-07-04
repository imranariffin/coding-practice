import java.util.Set;
import java.util.Map;
import java.util.HashMap;

class Counter<T> {
	private final 
	Map<T, Integer> counts = new HashMap<T, Integer>();

	public void add(T t) {
		counts.merge(t, 1, Integer::sum);
	}

	public int count(T t) {
		return counts.getOrDefault(t, 0);
	}

	public Set<T> keys() {
		return counts.keySet();
	}
}

class CanPermutePalindrome {
	public static boolean canPermutePalindrome(String s) {
		Counter<Character> counter = new Counter<Character>();
		for (char c: s.toCharArray()) {
			counter.add(c);
		}

		int nOdds = 0;
		for (Character c: counter.keys()) {
			if (counter.count(c)%2 != 0) {
				nOdds++;
			}
		}
		return nOdds < 2;
	}

	public static void main(String[] args) {
		String s = "abc";
		String ans = "false";
		System.out.format("s=%s\n\tAns: %s\n\tExpected: %s\n", 
			s, canPermutePalindrome(s), ans);

		s = "aba";
		ans = "true";
		System.out.format("s=%s\n\tAns: %s\n\tExpected: %s\n", 
			s, canPermutePalindrome(s), ans);
	}
}