class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        answer = [0,0]
        for i in range(1, n):
            b = n-i
            if '0' not in str(i) and '0' not in str(b) :
                answer[0] = i
                answer[1] = b
            pass
        return answer