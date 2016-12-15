public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m > 0 ? m - 1 : -1;
        int p2 = n > 0 ? n - 1 : -1;

        int p = m + n > 0 ? m + n - 1 : -1;

        while (p >= 0) {
            if (p1 < 0) {
                while (p2 >= 0) {
                    nums1[p--] = nums2[p2--];
                }

                break;
            }

            if (p2 < 0) {
                while (p1 >= 0) {
                    nums1[p--] = nums1[p1--];
                }

                break;
            }

            if (nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            }
            else {
                nums1[p--] = nums2[p2--];
            }
        }
    }
}
