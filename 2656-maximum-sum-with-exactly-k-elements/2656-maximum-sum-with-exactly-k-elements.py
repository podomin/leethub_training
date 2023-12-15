class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        answer = 0
        for i in range(k):
            answer += (max_num + i)
        return answer

            


        
        