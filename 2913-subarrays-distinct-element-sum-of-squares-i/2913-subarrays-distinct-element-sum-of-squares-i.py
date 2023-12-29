class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):  
                # value = len(set(nums[i:j]))
                # answer += value **2
                answer += (len(set(nums[i:j]))) ** 2
        return answer
        