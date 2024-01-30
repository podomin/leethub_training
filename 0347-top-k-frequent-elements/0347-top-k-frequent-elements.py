class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        answer = []
        c = Counter(nums)
        sort_c = c.most_common()
        for i in range(k):
            answer.append(sort_c[i][0])
        return answer
        