class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        word_slice = s.split(" ")
        answer = " ".join(word_slice[:k]) 
        return answer