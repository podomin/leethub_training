class Solution:
    def sortSentence(self, s: str) -> str:
        answer = []
        split_s = s.split(" ")
        sort_s = sorted(split_s, key=lambda x: int(x[-1]))
        for word in sort_s:
            answer.append(word[:-1])
        return " ".join(answer)
        
        