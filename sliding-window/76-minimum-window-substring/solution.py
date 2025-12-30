class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT, window = {}, {}
        for c in t: # update frequency of the map, what we need 
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # is our present character "useful" and are the counts equal?
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need: # do we have a valid substring?
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window while the window is valid to find a better answer
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""