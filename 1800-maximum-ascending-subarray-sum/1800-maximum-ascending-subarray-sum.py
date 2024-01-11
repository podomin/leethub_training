class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]: 
                prev = i
            print(nums[prev:i+1])
            s = sum(nums[prev:i+1])
            answer = max(s, answer)
        return answer
        