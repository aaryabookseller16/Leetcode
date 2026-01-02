from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict) #making wordDict a set for performance
        n = len(s) + 1

        # array to keep track of whether or not we can make words
        # up to a certain index
        dp = [False] * n
        dp[0] = True

        # cache
        trues = [0]

        # iterate through the string
        for i in range(1, n):
            for j in trues:
                # check if the words from j to i can be formed with wordDict
                if s[j:i] in wordDict:
                    # if yes, update the dp array
                    dp[i] = True
                    # update cache
                    trues.append(i)
                    break

        return dp[-1]