public class Solution {
    public int compareVersion(String version1, String version2) {
        int[] v1Arr = getVersionIntArray(version1);
        int[] v2Arr = getVersionIntArray(version2);
        
        return compareVersion(v1Arr, v2Arr);
    }
    
    private int compareVersion(int[] v1, int[] v2) {
        int p1 = 0;
        int p2 = 0;
        
        while (p1 < v1.length || p2 < v2.length) {
            int p1Num = p1 < v1.length ? v1[p1] : 0;
            int p2Num = p2 < v2.length ? v2[p2] : 0;
            
            if (p1Num > p2Num) {
                return 1;
            }
            else if (p1Num < p2Num) {
                return -1;
            }
            else {
                p1++;
                p2++;
            }
        }
        
        return 0;
    }
    
    private int[] getVersionIntArray(String version) {
        String[] sp = version.split("\\.");
        int[] res = new int[sp.length];
        
        for (int i = 0; i < res.length; i++) {
            res[i] = Integer.parseInt(sp[i]);
        }
        
        return res;
    }
}
