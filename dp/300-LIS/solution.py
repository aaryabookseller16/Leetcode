from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n #stores LIS upto a certain index

        if n == 0: # base case
            return 0

        # iterate through nums
        for i in range(1,n):
            # iterate from j to i and check for increasing subsequence
            for j in range(i):
                if nums[i] > nums[j]: # if increasing
                    dp[i] = max(dp[i], dp[j] + 1) # update max -> include/exclude
        
        print(dp)
        return max(dp)