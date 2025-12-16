from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            currSum += n # running sum
            diff = currSum -k

            # increment result if the subarray can sum upto k or else 0
            res += prefixSums.get(diff,0)

            # update the frequency of the prefix sum in our hashmap
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

        return res


        