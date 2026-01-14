from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            #if it is a start of a new sequence
            if num-1 not in num_set:
                temp_length = 1
                curr_head = num
                
                #keep updating as long as there is a consecutive sequence
                while curr_head + 1 in num_set:
                    curr_head += 1
                    temp_length += 1
                
                # check if current sequence is LCS or not
                longest = max(longest, temp_length)

        
        return longest

                    

        