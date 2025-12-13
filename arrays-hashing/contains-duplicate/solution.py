from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set can only store unique elements
        # therefore if our list and the set do not have the same length
        # that indicates that we had a duplicate element in our list
        return len(nums) != len(set(nums))