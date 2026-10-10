
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)

        for ch in t:
            counts[ch] -= 1

            if counts[ch] < 0:
                return ch
        