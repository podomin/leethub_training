class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a = word.find(ch,0)
        reverse = word[0:a+1]
        left = word[a+1:len(word)]
        answer = reverse[::-1] + left
        return answer
        