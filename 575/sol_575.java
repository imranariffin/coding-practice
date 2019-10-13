public class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> cset = new HashSet<>();
        for (int candy : candies) {
            cset.add(candy);
        }
        return Math.min(candies.length / 2, cset.size());
    }
}
