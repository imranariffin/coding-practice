import java.util.List;
import java.util.Collections;
import java.util.Comparator;

class Solution {
    public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return Math.abs(x - a) - Math.abs(x - b);
            }
        });
        
        List<Integer> kClosests = arr.subList(0, k);
        
        Collections.sort(kClosests, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return a - b;
            }
        });
        
        return kClosests;
    }
}
