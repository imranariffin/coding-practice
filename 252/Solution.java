/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */

import java.util.ArrayDeque;
import java.util.Iterator;
import java.util.Arrays;
 
public class Solution {
    public boolean canAttendMeetings(Interval[] intervals) {

        ArrayDeque<Interval>
            q = new ArrayDeque<Interval>();

        for (Interval i: intervals) {
            q.addFirst(i);
        }

        while (q.size()>0) {
            Interval i = q.removeFirst();
            for (Iterator<Interval> it=q.iterator(); it.hasNext();) {
                Interval j = it.next();
                if (!(i.end <= j.start || i.start >= j.end))
                    return false;
            }
        }
        return true;
    }

    public static void
    main(String[] args) {
        Solution s = new Solution();

        System.out.println("TEST 0");
        Interval[] intervals0 = {
            new Interval(0, 1), 
            new Interval(2, 3)
        };
        System.out.println(Arrays.toString(intervals0));
        assert s.canAttendMeetings(intervals0) == true;

        System.out.println("TEST 1");
        Interval[] intervals1 = {
            new Interval(0, 2), 
            new Interval(1, 3)
        };
        System.out.println(Arrays.toString(intervals1));
        assert s.canAttendMeetings(intervals1) == false;

        System.out.println("TEST 2");
        Interval[] intervals2 = {
            new Interval(0, 2), 
            new Interval(2, 3), 
            new Interval(3, 5), 
            new Interval(5, 8)
        };
        System.out.println(Arrays.toString(intervals2));
        assert s.canAttendMeetings(intervals2) == true;

        System.out.println("TEST 3");
        Interval[] intervals3 = {
            new Interval(0, 2), 
            new Interval(2, 4), 
            new Interval(3, 5), 
            new Interval(5, 8)
        };
        System.out.println(Arrays.toString(intervals3));
        assert s.canAttendMeetings(intervals3) == false;

        System.out.println("TEST 4");
        Interval[] intervals4 = {
            new Interval(0, 2), 
            new Interval(2, 4), 
            new Interval(3, 5), 
            new Interval(4, 8)
        };
        System.out.println(Arrays.toString(intervals4));
        assert s.canAttendMeetings(intervals4) == false;

        return;
    }
}