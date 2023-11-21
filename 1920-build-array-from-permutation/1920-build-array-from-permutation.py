class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        answer = []
        for i,num in enumerate(nums):
            print(i,num)
            answer.append(nums[nums[i]])
            
        return answer

        