class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        answer = ""
        mid = len(s) // 2
        for i in range(mid):
            # 두 알파벳 비교, 알파벳 순서상 더 작은거 선택
            selected = min(s[i], s[len(s) - i - 1])
            answer += selected
        # s 길이가 짝수일 때: answer + answer 뒤집은거
        if len(s) % 2 == 0:
            return answer + answer[::-1]
        # s 길이가 홀수일 때: answer + s[mid] + answer 뒤집은거
        else:
            return answer + s[mid] + answer[::-1]
    
        