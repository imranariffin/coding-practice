import java.util.Collections;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    public String reverseWords(String s) {
    	ArrayList<String> list = new ArrayList<String>(
    		Arrays.asList(s.trim().split(" +")));
    	Collections.reverse(list);
        return String.join(" ", list);
    }
}