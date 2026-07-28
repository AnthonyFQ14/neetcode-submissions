class Solution {
    public int countPrimes(int n) {
        
        if (n == 0 || n == 1){
            return 0;
        }

        int primes = 0;

        int [] nums = new int[n];
        Arrays.fill(nums,1);

        nums[0] = 0;
        nums[1] = 0;

        for (int num = 2; num < n; num++){
            if(nums[num] != 0){
                primes++;
                for(long i = (long) num * num; i < n; i += num){
                    nums[(int)i] = 0;
                }
            }
        }

        return primes;
    }
}