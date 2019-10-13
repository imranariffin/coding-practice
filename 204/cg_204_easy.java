public class Solution {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        
        for (int i = 2; i < primes.length; i++) {
            primes[i] = true;
        }
        
        for (int i = 0; i < primes.length; i++) {
            if (!primes[i]) {
                continue;
            }
            
            for (int j = 2 * i; j < primes.length; j += i) {
                primes[j] = false;
            }
        }
        
        int primeCount = 0;
        
        for (boolean p : primes) {
            if (p) {
                primeCount++;
            }
        }
        
        return primeCount;
    }
}
