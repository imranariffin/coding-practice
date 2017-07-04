import java.util.HashMap;

public class Logger {
    HashMap<String, Integer> history;

    /** Initialize your data structure here. */
    public Logger() {
        this.history = new HashMap<String, Integer>();
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        if (this.history.containsKey(message)) {
            if ((timestamp - this.history.get(message)) >= 10) {
                this.history.put(message, timestamp);
                return true;
            }
            return false;
        } 
        else {
            this.history.put(message, timestamp);
            return true;
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */