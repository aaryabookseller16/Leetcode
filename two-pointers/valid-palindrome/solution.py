import re
from typing import List

class Solution:
    # helper to remove unnecessary characters
    def removeExtras(self, s: str) -> str:
        cleaned_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return cleaned_s

    def isPalindrome(self, s: str) -> bool:
        i = 0
        cleaned_s = self.removeExtras(s)
        j = len(cleaned_s) - 1

        # compare elements from the start and the end
        while i < j:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i += 1
            j -= 1
        return True