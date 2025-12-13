from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #store value -> idx

        for i, value in enumerate(nums):
            diff = target - value
            if diff in map: # if we find the element and the difference
                return [map[diff], i]
            map[value] = i

        return []
            
