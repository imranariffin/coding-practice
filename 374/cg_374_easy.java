/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int s = 1;
        int e = n;
        int g = -1;
        boolean success = false;
        
        while (!success) {
            g = ((e - s) / 2) + s;
            
            int r = guess(g);
            
            switch (r) {
                case -1:
                    e = g - 1;
                    break;
                case 0:
                    success = true;
                    break;
                case 1:
                    s = g + 1;
                    break;
                default:
                    return -1;
            }
        }
        
        return g;
    }
}
