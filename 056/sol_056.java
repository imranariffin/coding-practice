/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> res = new LinkedList<>();
        if (intervals.size() < 1) {
            return res;
        }

        // Sorting ensures that if the bubble (interval) is to merge with the next bubble, the start
        // of the second bubble must be inside the first bubble. Sorting eliminates the case where
        // the start of second bubble to be < the start of the first bubble since we sort by start
        // value.
        intervals.sort((a, b) -> a.start - b.start);

        Interval bubble = new Interval(intervals.get(0).start, intervals.get(0).end);
        for (int i = 1; i < intervals.size(); ++i) {
            Interval interval = intervals.get(i);
            if (interval.start >= bubble.start && interval.start <= bubble.end) {
                bubble.end = Math.max(bubble.end, interval.end);
            } else {
                res.add(bubble);
                bubble = new Interval(interval.start, interval.end);
            }
        }
        res.add(bubble);
        return res;
    }
}
