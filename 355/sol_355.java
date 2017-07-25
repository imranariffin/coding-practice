public class Twitter {
    List<Integer[]> tweets;
    List<Set<Integer>> follows;

    /** Initialize your data structure here. */
    public Twitter() {
        this.tweets = new ArrayList<>();
        this.follows = new ArrayList<>();
    }

    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        tweets.add(new Integer[] { userId, tweetId });
    }

    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> rt = new LinkedList<>();
        int n = tweets.size();
        int tp = n - 1;
        int tc = 10;
        while (tc > 0 && tp >= 0) {
            Integer[] tweet = tweets.get(tp);
            if (tweet[0] == userId || (follows.size() > userId && follows.get(userId).contains(tweet[0]))) {
                rt.add(tweet[1]);
                tc--;
            }
            tp--;
        }
        return rt;
    }

    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        while (follows.size() <= followerId) {
            follows.add(new HashSet());
        }
        follows.get(followerId).add(followeeId);
    }

    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if (follows.size() <= followerId) return;
        follows.get(followerId).remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
