class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        split_s = s.split("|")
        for i in range(len(split_s)):
            if i % 2 == 0:
                cnt = split_s[i].count('*')
                answer += cnt
            else:
                pass
        return answer

        