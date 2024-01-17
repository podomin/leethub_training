class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        answer = 0
        c_nums = Counter(nums)
        for k,v in c_nums.items():
            if v == max(c_nums.values()):
                answer += v
        return answer
        