import java.util.HashMap;

class TrieNode {
	HashMap<Character, TrieNode> map;
	boolean ret;
	TrieNode() {
		map = new HashMap<Character, TrieNode>(26, 1);
		ret = false;
	}
}

public class Trie {
	TrieNode root;

	/** Initialize your data structure here. */
	public Trie() {
		root = new TrieNode();
	}

	/** Inserts a word into the trie. */
	public void insert(String word) {
		TrieNode node = root;
		char[] chArr = word.toCharArray();
		for (int i=0; i<word.length(); i++) {
			char c = chArr[i];
			if (node.map.containsKey(c)) {
				node = node.map.get(c);
			} else {
				node.map.put(c, new TrieNode());
				node = node.map.get(c);
			}
		}
		node.ret = true;
	}

	/** Returns if the word is in the trie. */
	public boolean search(String word) {
		TrieNode node = root;
		for (char c: word.toCharArray()) {
			if (node.map.containsKey(c)) {
				node = node.map.get(c);
			} else {
				return false;
			}
		}
		return node.ret;
	}

	// /** Returns if there is any word in the trie that starts with the given prefix. */
	public boolean startsWith(String prefix) {
		TrieNode node = root;
		for (char c: prefix.toCharArray()) {
			if (node.map.containsKey(c)) {
				node = node.map.get(c);
			} else {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		Trie trie = new Trie();
		String word = "word";
		boolean ans = trie.search(word);
		boolean exp = false;
		String good = ">>> %s(%s)\nans == exp : %s == %s GOOD\n";
		String bad = ">>> %s(%s)\nans != exp : %s != %s BAD!\n";
		String print = ans == exp ? good : bad;
		System.out.format(print, "search", word, ans, exp);

		word = "word";
		System.out.format(">>> insert(%s)\n", word);
		trie.insert(word);
		ans = trie.search(word);
		exp = true;
		print = ans == exp ? good : bad;
		System.out.format(print, "search", word, ans, exp);

		word = "word2";
		ans = trie.search(word);
		exp = false;
		print = ans == exp ? good : bad;
		System.out.format(print, "search", word, ans, exp);

		word = "longword";
		System.out.format(">>> insert(%s)\n", word);
		trie.insert(word);
		word = "long";
		ans = trie.startsWith(word);
		exp = true;
		print = ans == exp ? good : bad;
		System.out.format(print, "startsWith", word, ans, exp);

		word = "ab";
		System.out.format(">>> insert(%s)\n", word);
		trie.insert(word);
		word = "a";
		ans = trie.search(word);
		exp = false;
		print = ans == exp ? good : bad;
		System.out.format(print, "search", word, ans, exp);
	}
}