import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;
import java.util.Arrays;


class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ret = new ArrayList<>();
        _permute(ret, nums, 0);
        return ret;
    }
    
    private void _permute(List<List<Integer>> ret, int[] nums, int i) {
        for (int j = i; j < nums.length; j++) {
            _swap(nums, i, j);
            if (i >= nums.length - 1) {
                ret.add(Arrays.stream(nums).boxed().collect(Collectors.toList()));
            } else {
                _permute(ret, nums, i + 1);
            }
            _swap(nums, i, j);
        }
    }
    
    private void _swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
