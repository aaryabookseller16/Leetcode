class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # define cache
        dp = [0]*n

        #add base cases to cache
        dp[0] = 1
        dp[1] = 2


        #loop from 2 to n
        for i in range(2,n):
            # add previous 2 elements to present element
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]