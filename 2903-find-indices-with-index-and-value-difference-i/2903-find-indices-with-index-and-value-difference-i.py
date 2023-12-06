class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 2중 for 문을 enumerate 같이 사용
        answer = []
        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return[i,j]

        return [-1,-1]



        