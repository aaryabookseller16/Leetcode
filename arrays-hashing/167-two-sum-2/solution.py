from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difference_map = {} # number -> index


        for i in range(len(numbers)):
            difference = target - numbers[i]

            if difference in difference_map:
                return [difference_map[difference] + 1, i + 1]
            
            #add number->index pair after in order to avoid duplication and not violate question condition
            difference_map[numbers[i]] = i 

        return []        