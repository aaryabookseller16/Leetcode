from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        left = 0
        right = 0
        runningSum = 0

        while right < len(nums):
            runningSum += nums[right]   # expand window
            right += 1

            while runningSum >= target: # shrink as much as possible for min.
                best = min(best, right - left)
                runningSum -= nums[left]
                left += 1

        return 0 if best == float('inf') else best