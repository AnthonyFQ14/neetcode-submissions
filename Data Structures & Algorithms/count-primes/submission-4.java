class Solution {
    public int countPrimes(int n) {
        
        if (n < 3) return 0;

        boolean [] nums = new boolean[n];

        int primes = 0;

        for (int i = 2; i < n; i++){
            if(!nums[i]){
                primes++;

                for (long j = (long) i * i; j < n; j += i){
                    nums[(int)j] = true;
                }
            }
        }

        return primes;

    }
}