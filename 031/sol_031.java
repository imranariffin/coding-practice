/**
 * Refer to this amazing age-old algorithm by Narayana Pandit in Wikipedia
 * (https://en.wikipedia.org/wiki/Permutation#Algorithms_to_generate_permutations).
 */
public class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int k = n - 2;
        while (k >= 0) {
            if (nums[k] < nums[k + 1]) break;
            k--;
        }
        if (k < 0) {
            reverse(nums, 0, n - 1);
            return;
        }
        int l = n - 1;
        while (nums[k] >= nums[l]) {
            l--;
        }
        swap(nums, k, l);
        reverse(nums, k + 1, n - 1);
    }

    private void swap(int[] arr, int p1, int p2) {
        int tmp = arr[p1];
        arr[p1] = arr[p2];
        arr[p2] = tmp;
    }

    private void reverse(int[] arr, int p1, int p2) {
        while (p1 < p2) {
            swap(arr, p1, p2);
            p1++;
            p2--;
        }
    }
}
