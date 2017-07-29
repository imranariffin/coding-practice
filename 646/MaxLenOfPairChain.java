import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Collections;
import java.util.Comparator;

class Pair {
    public int first;
    public int second;
    
    public Pair(int a, int b) {
        first = a; second = b;
    }
    
    public String toString() {
        return "(" + first + "," + second + ")";
    }
}

public class Solution {
    public int findLongestChain(int[][] pairs) {
        List<int[]> listPair = Arrays.asList(pairs);
        
        List<Pair> ls = Arrays
            .asList(pairs)
            .stream()
            .map(x -> new Pair(x[0], x[1]))
        .collect(Collectors.toList());

        ls.sort(Comparator.comparing(x -> x.second));

        int n = 1;
        int bPrev = ls.get(0).second;
        int aCur;
        for (int i = 0; i < ls.size(); i++) {
            aCur = ls.get(i).first;
            if (aCur > bPrev) {
                n++;
                bPrev = ls.get(i).second;
            }
        }
        
        return n;
    }
}