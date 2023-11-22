class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        answer = None
        s_count = Counter(s)
        t_count = Counter(t)
        a = t_count-s_count
        for k,v in a.items():
            return k

        


        