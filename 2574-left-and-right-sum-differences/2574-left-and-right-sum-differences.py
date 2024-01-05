class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            lr_sum = sum(nums[0:i]) - sum(nums[i+1:len(nums)])
            answer.append(abs(lr_sum))
        return answer
        