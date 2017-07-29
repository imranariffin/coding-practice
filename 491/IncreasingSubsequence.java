import java.util.List;
import java.util.ArrayList;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

public class IncreasingSubsequence {
    Set<List<Integer>> set = new HashSet<List<Integer>>();
    List<Integer> subSeq = new ArrayList<Integer>();
        
    public List<List<Integer>> findSubsequences(int[] nums) {
        findSequence(0, nums);
        return new ArrayList(set);
    }
    
    private void findSequence(int i, int[] nums) {
        if (subSeq.size() >= 2) {
            set.add(new ArrayList(subSeq));
        }
        
        for (int j = i; j < nums.length; j++) {
            if (subSeq.size() == 0 || subSeq.get(subSeq.size() - 1) <= nums[j]) {
                subSeq.add(nums[j]);
                findSequence(j + 1, nums);
                subSeq.remove(subSeq.size() - 1);  
            }
        }
    }
}