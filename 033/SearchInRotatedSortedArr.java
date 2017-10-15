import java.util.Arrays;

public class SearchInRotatedSortedArr {
  public static int search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return -1;
    }
    int rot = findRotationMagnitude(nums);
    return binSearch(nums, target, rot);
  }

  private static int findRotationMagnitude(int[] nums) {
    int i = 0, j = nums.length - 1;

    // find size of rotation: eqv to finding min
    int rot = 0;
    while (i < j) {
      int mid = i + (j - i) / 2;
      if (nums[mid] < nums[j]) {
        j = mid;
      } else {
        i = mid + 1;
      }
    }
    rot = i;
    return rot;
  }

  private static int binSearch(int[] nums, int target, int rot) {
    // bin search with rotation magnitude
    int i = 0, j = nums.length;
    while (i < j) {
      int mid = i + (j - i) / 2;
      int realmid = (mid + rot) % nums.length;
      if (nums[realmid] < target) {
        i = mid + 1;
      } else if (nums[realmid] > target) {
        j = mid;
      } else {
        return realmid;
      }
    }
    return -1;
  }

  public static void main(String[] args) {
// {4,5,6,1,2,3} 4 -> 0
    int[] nums = {4,5,6,1,2,3};
    int target = 4;
    int ans = search(nums, target);
    int exp = 0;
    String printStr = "nums: %s, target: %s\n ans: %s\n exp: %s\n";
    System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// {4,5,6,1,2,3} 6 -> 2
    target = 6;
    ans = search(nums, target);
    exp = 2;
    System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// {4,5,6,1,2,3} 5 -> 1
    target = 5;
    ans = search(nums, target);
    exp = 1;
    System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// {4,5,6,1,2,3} 3 -> 5
    target = 3;
    ans = search(nums, target);
    exp = 5;
    System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// {4,5,6,1,2,3} 1 -> 3
    target = 1;
    ans = search(nums, target);
    exp = 3;
    System.out.format(printStr, Arrays.toString(nums), target, ans, exp);
// {6,1,2,3,4,5} 1 -> 3
    int[] nums2 = {6,1,2,3,4,5};
    target = 6;
    ans = search(nums2, target);
    exp = 0;
    System.out.format(printStr, Arrays.toString(nums2), target, ans, exp);
// {6,1,2,3,4,5} 3 -> 5
    target = 3;
    ans = search(nums2, target);
    exp = 3;
    System.out.format(printStr, Arrays.toString(nums2), target, ans, exp);
// {6,1,2,3,4,5} 1 -> 1
    target = 1;
    ans = search(nums2, target);
    exp = 1;
    System.out.format(printStr, Arrays.toString(nums2), target, ans, exp);
  }
}