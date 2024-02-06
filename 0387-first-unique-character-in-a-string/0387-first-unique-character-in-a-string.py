class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i,letter in enumerate(s):
            if c[letter] == 1:
                return i
                break
        return -1

        