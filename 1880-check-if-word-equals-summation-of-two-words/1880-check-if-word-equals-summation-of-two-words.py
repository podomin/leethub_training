class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word):
            str_c = ""
            for c in word:
                str_c += str(ord(c) - 97) 
            return int(str_c)
        return convert(firstWord) + convert(secondWord) == convert(targetWord)

        

        