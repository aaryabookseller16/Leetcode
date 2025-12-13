class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # stores the last idx where a char appeared
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            #if the current char is a duplicate
            if char in seen and seen[char] >= left:
                left = seen[char] + 1 # increment left
            
            seen[char] = right #update substring
            max_len = max(max_len, right-left+1) # update max len

        return max_len