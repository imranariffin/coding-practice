import java.util.Collections;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Comparator;

public class Solution {

	private class CounterTuple {
		public int val;
		public int freq;

		public CounterTuple(int val, int freq) {
			this.val = val;
			this.freq = freq;
		}

		public int compareTo(CounterTuple other) {
			if (freq < other.freq) {
				return -1;
			} else if (freq > other.freq) {
				return 1;
			} else {
				return 0;
			}
		}
	}

	public List<Integer> topKFrequent(int[] nums, int k) {
		HashMap<Integer, int[]> counter = new HashMap<Integer, int[]>();
		for (int n: nums) {
			int[] fa = counter.get(n);

			if (fa != null) {
				fa[0]++;
			} else {
				counter.put(n, new int[] {1});
			}
		}

		ArrayList<CounterTuple> aList = new ArrayList<CounterTuple>();
		for (Object key: counter.keySet().toArray()) {
			aList.add(new CounterTuple((Integer)key, counter.get(key)[0]));
		}

		// sort in reverse
		Collections.sort(aList, new Comparator<CounterTuple>() {
			@Override
			public int compare(CounterTuple ct1, CounterTuple ct2) {
				return ct2.compareTo(ct1);
			}
		});

		List<Integer> ret = new ArrayList<Integer>();
		for (int i=0; i<k; i++) {
			ret.add(aList.get(i).val);
		}
		return ret;
	}
}