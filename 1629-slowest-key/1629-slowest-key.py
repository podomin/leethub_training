class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        from collections import defaultdict
        dic = defaultdict(int)
        prev = 0
        for i, time in enumerate(releaseTimes):
            duration = time - prev
            prev = time
            dic[keysPressed[i]] = max(dic[keysPressed[i]], duration)
        ansser = ""
        cur_max = 0
        for k,v in dic.items():
            if v > cur_max:
                answer = k
                cur_max = v
            elif v == cur_max and answer < k:
                answer = k
        return answer



        