class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        answer = ""
        sort_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        for k,v in sort_c:
            answer += (k*v)
        return answer
        