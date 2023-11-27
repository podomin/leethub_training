class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        for i, word in enumerate(words):
            # 문자 x가 word 안에 포함되어 있는지 검사
            # 포함되어 있으면 answer에 추가
            if x in word:
                answer.append(i)
        return answer
            
        