import java.lang.StringBuilder;

public class ReverseStringII {
    public static String reverseStr(String s, int k) {
        char[] chArr = s.toCharArray();
        int n = chArr.length;
        int i = 0;
        while (i < n) {
            int j = Math.min(i + k, n);
            swap(chArr, i, j);
            i += 2*k;
        }
        return new String(chArr);
    }

    private static void swap(char[] chArr, int i, int j) {
        while (i < j) {
            char temp = chArr[j-1];
            chArr[j-1] = chArr[i];
            chArr[i] = temp;
            i++; j--;
        }
    }

    public static void main(String[] args) {
        String s = "abcdefg"; 
        int k = 2;
        String ans = reverseStr(s, k);
        String exp = "bacdfeg";
        String printStr = "s=%s, k=%s\nAns: %s\nExpected: %s\n";
        System.out.format(printStr, k, s, ans, exp);

        s = "abcd"; k = 1;
        ans = reverseStr(s, k);
        exp = "abcd";
        printStr = "s=%s, k=%s\nAns: %s\nExpected: %s\n";
        System.out.format(printStr, k, s, ans, exp);

        s = "abcdefghijklmnop"; k = 2;
        ans = reverseStr(s, k);
        exp = "bacdfeghjiklnmop";
        printStr = "s=%s, k=%s\nAns: %s\nExpected: %s\n";
        System.out.format(printStr, k, s, ans, exp);
    }
}