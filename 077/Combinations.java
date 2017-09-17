import java.util.List;
import java.util.ArrayList;


class Solution {    
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> combs = new ArrayList<>();
        _combine(combs, new ArrayList<>(), 1, n, k);
        return combs;
    }
    
    private void _combine(List<List<Integer>> combs, List<Integer> comb, int i, int n, int k) {
        if (k == 0) {
            combs.add(new ArrayList(comb));
            return;
        }
        for (int j = i; j <= n; j++) {
            comb.add(j);
            _combine(combs, comb, j + 1, n, k - 1);
            comb.remove(comb.size() - 1);
        }
    }
}
