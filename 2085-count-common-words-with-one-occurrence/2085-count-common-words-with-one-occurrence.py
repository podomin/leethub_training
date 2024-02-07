class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        c_1 = Counter(words1)
        c_2 = Counter(words2)
        word_set = set(words1 + words2)
        for word in word_set:
            if c_1[word] == 1 and c_2[word] == 1:
                print(word)
                answer += 1
        return answer
        