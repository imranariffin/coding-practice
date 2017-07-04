class Test {

	public static void main(String args[]) {
		Solution sol = new Solution();
		String s0 = "the sky is blue";
		String ans0 = "blue is sky the";
		String ret0 = sol.reverseWords(s0);
		assert ret0.equals(ans0): ret0 + "!=" + ans0;

		String s1 = " ";
		String ans1 = "";
		String ret1 = sol.reverseWords(s1);
		assert ret1.equals(ans1): ret1 + "!=" + ans1;
		assert 
			ret1.length() == ans1.length(): 
			"length: " + ret1.length() + "!=" + ans1.length();

		String s2 = "abc def";
		String ans2 = "def abc";
		String ret2 = sol.reverseWords(s2);
		assert ret2.equals(ans2): ret2 + "!=" + ans2;
		assert 
			ret2.length() == ans2.length(): 
			"length: " + ret2.length() + "!=" + ans2.length();

		String s3 = "   ";
		String ans3 = "";
		String ret3 = sol.reverseWords(s3);
		assert ret3.equals(ans3): ret3 + "!=" + ans3;
		assert 
			ret3.length() == ans3.length(): 
			"length: " + ret3.length() + "!=" + ans3.length();

		String s4 = " 1";
		String ans4 = "1";
		String ret4 = sol.reverseWords(s4);
		assert ret4.equals(ans4): ret4 + "!=" + ans4;
		assert 
			ret4.length() == ans4.length(): 
			"length: " + ret4.length() + "!=" + ans4.length();
	}
}