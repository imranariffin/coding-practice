public class RomanToInteger {

	public static int romanToInt(String roman) {
		int len = roman.length();
		char[] romanChars = roman.toCharArray();
		int ret = 0;
		for (int i = 0; i < len; i++) {
			char c = romanChars[i];
			int curr = eval(c);
			if (curr == -1) return -1;
			if (i < len - 1 && curr < eval(romanChars[i + 1])) {
				ret += eval(romanChars[i + 1]) - curr;
				i++;
			} else {
				ret += curr;
			}
		}
		return ret;
	}

	private static int eval(char c) {
		switch (c) {
			case 'I': return 1;
			case 'V': return 5;
			case 'X': return 10;
			case 'L': return 50;
			case 'C': return 100;
			case 'D': return 500;
			case 'M': return 1000;
			default: return -1;
		}
	}

	public static void main(String[] args) {
		String s = "X";
		String str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		int expected = 10;
		int answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "XIII";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 13;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "IX";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 9;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "III";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 3;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "I";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 1;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "II";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 2;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "III";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 3;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "IV";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 4;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);

		s = "XIV";
		str = ">>>\nInput: %s\nAns: %s\nExpected %s\n";
		expected = 14;
		answer = romanToInt(s);
		System.out.format(str, s, answer, expected);
	}
}