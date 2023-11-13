class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # 1.  words 배열을 순회하면서 각 단어별 첫 번째 글자
        # 2. 각 단어별 첫 번째 글자들로 이루어진 단어 만들기
        # 3. 그렇게 만든 단어가 s와 동일한지 비교해보기
        acronym = ""
        for word in words:
            acronym += word[0]
        print(acronym)
        if acronym == s:
            return True
        return False
            


