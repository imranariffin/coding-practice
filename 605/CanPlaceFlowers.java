// class Solution {
// public:
//     bool canPlaceFlowers(vector<int>& flowerbed, int n) {
//         int m = 0, c = 1;
//         for (int i: flowerbed) {
//             if (i == 0) {
//                 ++c;
//             } else {
//                 m += (c - 1) / 2;
//                 c = 0;
//             }
//         }
//         ++c;
//         m += (c - 1) / 2;
//         return m >= n;
//     }
// };

import java.util.Arrays;

public class CanPlaceFlowers {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int m = 0, count = 1;
        for (int e: flowerbed) {
            if (e == 0) {
                count++;
            }
            else {
                m += (count - 1) / 2;
                count = 0;
            }
        }
        count++;
        m += (count - 1) / 2;
        return m >= n;
    }

    public static void main(String[] args) {
        String printStr = "flowerbed = %s, n=%d\nAns: %s\nExpected: %s\n";
     
        int[] flowerbed = {1,0,0,0,1};
        int n = 1;
        String s = Arrays.toString(flowerbed);
        boolean ans = canPlaceFlowers(flowerbed, n);
        boolean expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed2 = {1,0,0,0,1};
        n = 2;
        s = Arrays.toString(flowerbed2);
        ans = canPlaceFlowers(flowerbed2, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed3 = {1,0,1,0,1};
        n = 1;
        s = Arrays.toString(flowerbed2);
        ans = canPlaceFlowers(flowerbed3, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed4 = {1,0,0,0,0,1};
        n = 1;
        s = Arrays.toString(flowerbed4);
        ans = canPlaceFlowers(flowerbed4, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed5 = {1,0,0,0,0,1};
        n = 2;
        s = Arrays.toString(flowerbed5);
        ans = canPlaceFlowers(flowerbed5, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed6 = {1,0,0,1};
        n = 1;
        s = Arrays.toString(flowerbed6);
        ans = canPlaceFlowers(flowerbed6, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed7 = {1,0,0,0,0,0,1};
        n = 1;
        s = Arrays.toString(flowerbed7);
        ans = canPlaceFlowers(flowerbed7, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed8 = {1,0,0,0,0,0,1};
        n = 2;
        s = Arrays.toString(flowerbed8);
        ans = canPlaceFlowers(flowerbed8, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed9 = {1,0,0,1,0,0,1};
        n = 1;
        s = Arrays.toString(flowerbed9);
        ans = canPlaceFlowers(flowerbed9, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed10 = {0,0,0,1,0,0,1};
        n = 1;
        s = Arrays.toString(flowerbed10);
        ans = canPlaceFlowers(flowerbed10, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed11 = {1,0,0,1,0,0,0};
        n = 1;
        s = Arrays.toString(flowerbed11);
        ans = canPlaceFlowers(flowerbed11, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed12 = {0};
        n = 1;
        s = Arrays.toString(flowerbed12);
        ans = canPlaceFlowers(flowerbed12, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed13 = {0,0};
        n = 1;
        s = Arrays.toString(flowerbed13);
        ans = canPlaceFlowers(flowerbed13, n);
        expected = true;
        System.out.format(printStr, s, n, ans, expected);

        int[] flowerbed14 = {0,0};
        n = 2;
        s = Arrays.toString(flowerbed14);
        ans = canPlaceFlowers(flowerbed14, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);

       int[] flowerbed15 = {1};
        n = 0;
        s = Arrays.toString(flowerbed15);
        ans = canPlaceFlowers(flowerbed15, n);
        expected = false;
        System.out.format(printStr, s, n, ans, expected);
    }
}