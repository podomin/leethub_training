class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        sort_num = sorted(nums)
        for i, num in enumerate(sort_num):
            if num == target:
                answer.append(i)
        return answer
        