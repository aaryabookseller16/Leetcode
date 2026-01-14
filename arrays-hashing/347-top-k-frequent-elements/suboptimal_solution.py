from collections import Counter
from typing import List
from itertools import islice


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums) #make a frequency map

        # sort it and return top k
        freq_map = dict(sorted(freq_map.items(), key = lambda item: item[1], reverse = True))
        first_k_list = list(islice(freq_map, k))

        return first_k_list
        