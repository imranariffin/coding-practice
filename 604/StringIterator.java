import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;

public class StringIterator {

	class Pair {
		public char c;
		public int f;
		Pair(char _c, int _f) {
			c = _c; f = _f;
		}
	}

	private LinkedList<Pair> list = new LinkedList<Pair>();

	public StringIterator(String compressedString) {
		int n = compressedString.length();
		char[] s = compressedString.toCharArray();

		for (int i=0; i<n; ) {
			char c = s[i++];
			int f = 0;
			while (i < n && s[i] >= '0' && s[i] <= '9') {
				f = f*10 + s[i] - '0';
				i++;
			}
			list.add(new Pair(c, f));
		}
	}

	public char next() {
		if (hasNext()) {
			Pair p = list.peek();
			if (p.f == 1) {
				list.poll();
				return p.c;
			}
			p.f--;
			return p.c;
		}
		return ' ';
	}

	public boolean hasNext() {
		if (list.size() == 0) {
			return false;
		}
		return list.peek().f > 0;
	}

	public static void main(String[] args) {
		StringIterator it = new StringIterator("L1e2t1C1o1d1e1");
		while (it.hasNext()) {
			System.out.println(it.next());
		}

		// ["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]
		// [["L2e2t2C2o2d2e23"],[],[],[],[],[],[],[],[],[]]

		StringIterator it2 = new StringIterator("L2e2t2C2o2d2e23");
		System.out.println(it2.next());
		System.out.println(it2.next());
		System.out.println(it2.next());
		System.out.println(it2.next());
		System.out.println(it2.next());
		System.out.println(it2.next());

		System.out.println(it2.hasNext());

		System.out.println(it2.next());

		System.out.println(it2.hasNext());
	}
}

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator obj = new StringIterator(compressedString);
 * char param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */


/*
Author: wcwswswws

class StringIterator {
public:
    StringIterator(string compressedString) {
        int len = compressedString.length();
        for (int i = 0; i < len;) {
            pair<char, int> temp;
            temp.first = compressedString[i++];
            temp.second = 0;
            while (i < len && compressedString[i] >= '0' && compressedString[i] <= '9') {
                temp.second = temp.second * 10 + compressedString[i++] - '0';
            }
            str.push_back(temp);
        }
        cur_ = num_ = 0;
    }
    
    char next() {
        if (cur_ < str.size()) {
            char ans = str[cur_].first;
            if (num_ + 1 == str[cur_].second) {
                num_ = 0;
                cur_++;
            } else {
                num_++;
            }
            return ans;
        } else {
            return ' ';
        }
    }
    
    bool hasNext() {
        return (cur_ < str.size());
    }
private:
    vector< pair<char, int> > str;
    int cur_, num_;
};

*/