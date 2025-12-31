class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1: # s1 cannot be greater than s2
            return False
    
        freq1 = [0]*26
        freq2 = [0]*26

        for i in range(len(s1)): # update frequency count array for s1
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1 # our initial window
        
        if freq1 == freq2: # if the first window is our permutation
            return True
        
        for i in range(n1, n2):
            freq2[ord(s2[i]) - ord('a')] += 1

            # we want to lose the character at the (i-n1)th position
            freq2[ord(s2[i-n1]) - ord('a')] -= 1

            if freq1 == freq2:
                return True
            
        return False