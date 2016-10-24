public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> L = new ArrayList<Integer>();
        
        int p1 = 0;
        int p2 = 0;
        
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        while (p1 < nums1.length && p2 < nums2.length) {
            if (nums1[p1] == nums2[p2]) {
                L.add(nums1[p1]);
                p1 = moveRight(nums1, p1);
                p2 = moveRight(nums2, p2);
            }
            else if (nums1[p1] < nums2[p2]) {
                p1 = moveRight(nums1, p1);
            }
            else {
                p2 = moveRight(nums2, p2);
            }
        }
        
        int[] res = new int[L.size()];
        
        for (int i = 0; i < L.size(); i++) {
            res[i] = L.get(i);
        }
        
        return res;
    }
    
    private int moveRight(int[] nums, int p) {
        p++;
        
        return p;
    }
}
