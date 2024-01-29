class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        str_n = str(n)
        for c in range(len(str_n)):
            if c % 2 == 0:
                answer += int('+' + str_n[c])
            else: 
                answer += int('-' + str_n[c])
        return answer
        