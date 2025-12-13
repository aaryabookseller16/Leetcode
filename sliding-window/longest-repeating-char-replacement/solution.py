class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        counts = [0] * 26  # char -> freq

        for right in range(len(s)):
            # get the correct index of an alphabet in the string
            # by subtracting its ASCII value by 65
            # eg: ASCII of 'B' is 66 so we will increment
            # index 1 of array by 1
            counts[ord(s[right]) - 65] += 1

            # while the window is invalid:
            # we have more than k chars to replace
            while (right - left + 1) - max(counts) > k:
                # remove left most char from our window
                counts[ord(s[left]) - 65] -= 1
                left += 1

            # while window is valid
            longest = max(longest, right - left + 1)

        return longest