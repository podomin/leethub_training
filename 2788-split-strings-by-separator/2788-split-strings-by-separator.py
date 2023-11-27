class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            split_word_list = word.split(separator)
            print(split_word_list)
            for split_word in split_word_list:
                if split_word is not "":
                    answer.append(split_word)
                pass
        return answer
        