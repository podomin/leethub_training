class Solution:
    def countPoints(self, rings: str) -> int:
        from collections import defaultdict
        answer = 0
        d = defaultdict(set)

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings [i+1]
            d[rod].add(color)
        print(d)
        for k, v in d.items():
            if len(v) == 3:
                answer += 1
        return answer
        