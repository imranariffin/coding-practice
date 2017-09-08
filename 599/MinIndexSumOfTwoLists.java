import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class MinIndexSumOfTwoLists {
    public String[] findRestaurant(String[] list1, String[] list2) {
        List<String> l1 = new ArrayList<>(Arrays.asList(list1));
        List<String> l2 = new ArrayList<>(Arrays.asList(list2));
        Set<String> s1 = new HashSet<>();
        Set<String> s2 = new HashSet<>();
        Set<String> s = new HashSet<>();
        Map<String, Integer> m = new HashMap<>();
        
        /* get the intersection set */
        for (String x: l1) {
            s1.add(x);
        }
        for (String x: l2) {
            s2.add(x);
        }
        for (String x: s1) {
            if (s2.contains(x)) {
                s.add(x);
            }
        }
        
        /* get minimum sum of index and build the sum map*/
        int minsum = 2000;
        for (String x: s) {
            int sum = l1.indexOf(x) + l2.indexOf(x);
            m.put(x, sum);
            if (sum < minsum) minsum = sum;
        }
        
        /* get all string that has sum equal to min sum */
        List<String> ret = new ArrayList<>();
        for (String x: m.keySet()) {
            if (m.get(x) == minsum) {
                ret.add(x);
            }
        }
        
        return ret.toArray(new String[ret.size()]);
    }
}
