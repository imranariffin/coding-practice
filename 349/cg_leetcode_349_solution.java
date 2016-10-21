public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int p1 = 0;
        int p2 = 0;
        ArrayList<Integer> res = new ArrayList<Integer>();
        
        while (p1 < nums1.length && p2 < nums2.length) {
            if (nums1[p1] == nums2[p2]) {
                res.add(nums1[p1]);
                p1 = nextPointer(nums1, ++p1);
                p2 = nextPointer(nums2, ++p2);
            }
            else if (nums1[p1] < nums2[p2]) {
                p1 = nextPointer(nums1, ++p1);
            }
            else {
                p2 = nextPointer(nums2, ++p2);
            }
        }
        
        int[] resArr = new int[res.size()];
        Iterator<Integer> it = res.iterator();
        
        for (int i = 0; i < resArr.length; i++) {
            resArr[i] = it.next().intValue();
        }
        
        return resArr;
    }
    
    private int nextPointer(int[] arr, int curr) {
        while (curr < arr.length) {
            if (curr > 0 && arr[curr] != arr[curr - 1]) {
                return curr;
            }
            
            curr++;
        }
        
        return curr;
    }
}
