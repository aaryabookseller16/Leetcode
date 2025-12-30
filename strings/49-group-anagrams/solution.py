from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a default dict
        anagrams_dict = defaultdict(list)

        # loop through each string
        for s in strs:
            # create a frequency count for each string
            freq = [0]*26

            # loop through chars in each string
            for c in s:
                #update frequency of chars using ord
                freq[ord(c) - ord('a')] += 1

            # convert array to tuple for immmutability
            key = tuple(freq)
            # use tuple as key in our default dict and append string
            anagrams_dict[key].append(s)
        
        # return values of our default dict
        return list(anagrams_dict.values())