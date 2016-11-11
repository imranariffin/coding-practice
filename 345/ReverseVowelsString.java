class ReverseVowelsString {
	String reverseVowels(String s) {
		char[] charArr;
		charArr = s.toCharArray();

		// collect all vowels in reverse
		StringBuilder vowelSB = new StringBuilder();
		for (char c: charArr) {
			if ("AEIOUaeiou".indexOf(c) >= 0)
				vowelSB.insert(0, c);
		}

		// fill in vowels appropriately
		StringBuilder ret = new StringBuilder();
		int i = 0;
		for (char c: charArr) {
			if ("AEIOUaeiou".indexOf(c) >= 0) {
				ret.append(vowelSB.charAt(i));
				i++;
			}
			else ret.append(c);
		}
		return ret.toString();
	}

	public static void main(String args[]) {
		ReverseVowelsString rvs = new ReverseVowelsString();
		
		String say = "Hello World!";
		System.out.println(say);
		System.out.println(rvs.reverseVowels(say));

		return;
	}
}