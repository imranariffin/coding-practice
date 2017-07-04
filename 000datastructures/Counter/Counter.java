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