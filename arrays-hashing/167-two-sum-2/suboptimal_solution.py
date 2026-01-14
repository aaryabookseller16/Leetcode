from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #inefficient solution
        for i in range(len(numbers)):
            difference = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j] == difference:
                    return [i + 1, j + 1]
        
        return []