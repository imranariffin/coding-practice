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
    public boolean canAttendMeetings(Interval[] intervals) {
        if (intervals.length < 1) {
            return true;
        }
        ArrayList<Interval> occupied = new ArrayList<Interval>();
        
        Arrays.sort(intervals, (x,y) -> -(new Integer(x.end - x.start).compareTo(y.end - y.start)));
        
        for (int i = 0; i < intervals.length; i++) {
            Interval meeting = intervals[i];
            
            for (int j = 0; j < occupied.size(); j++) {
                Interval scheduledMeeting = occupied.get(j);
                
                if (meeting.start == scheduledMeeting.start && meeting.end == scheduledMeeting.end) {
                    return false;
                }
                
                if (meeting.start > scheduledMeeting.start && meeting.start < scheduledMeeting.end) {
                    return false;
                }
                
                if (meeting.end > scheduledMeeting.start && meeting.end < scheduledMeeting.end) {
                    return false;
                }
            }
            
            occupied.add(meeting);
        }
        
        return true;
    }
}
