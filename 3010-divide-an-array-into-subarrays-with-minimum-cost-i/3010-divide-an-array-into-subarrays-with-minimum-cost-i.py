class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = 10000
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                part_one = nums[:i]
                part_two = nums[i:j]
                part_three = nums[j:]
                # print(part_one, part_two, part_three)
                all = part_one[0] + part_two[0] + part_three[0]
                answer = min(answer, all)
        return answer
        