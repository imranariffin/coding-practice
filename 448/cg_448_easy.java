public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> nSet = new HashSet<>();

        for (int i = 1; i <= nums.length; i++) {
            nSet.add(i);
        }

        for (int i = 0; i < nums.length; i++) {
            if (nSet.contains(nums[i])) {
                nSet.remove(nums[i]);
            }
        }

        List<Integer> res = new ArrayList<>();
        Iterator<Integer> it = nSet.iterator();

        while (it.hasNext()) {
            res.add(it.next());
        }

        return res;
    }
}
