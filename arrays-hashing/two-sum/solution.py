class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_index = {} # keeps track of number -> index
        answer = []

        for i in range(len(nums)): # O(n)
            difference = target - nums[i]

            # check before updating the map, in order to avoid duplicates
            if difference in n_index: # O(1)
                answer.append(i) # append current index
                answer.append(n_index[difference]) # append index of corresponding element
                return answer
            
            # if difference is not present, just store the n -> index pair
            # for future use
            n_index[nums[i]] = i

        return []

# Overall time complexity: O(n)
# Overall space complexity: O(n)
