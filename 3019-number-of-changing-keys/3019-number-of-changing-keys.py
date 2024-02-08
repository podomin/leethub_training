class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        low_s = s.lower()
        prev = 0
        for c in range(1, len(low_s)):
            if low_s[prev] != low_s[c]:
                answer += 1
                prev = c
            else:
                prev = c
        return answer
        