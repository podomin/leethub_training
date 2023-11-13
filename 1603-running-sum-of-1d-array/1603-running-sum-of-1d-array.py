class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        running_sum = 0
        for num in nums:
            running_sum += num
            answer.append(running_sum)
        return answer


