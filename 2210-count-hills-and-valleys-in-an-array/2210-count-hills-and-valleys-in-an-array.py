class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        # 연속된 숫자 제거
        new_nums = [nums[0]]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                new_nums.append(nums[i])
                prev = nums[i]
        print(new_nums)
        for j in range(1, len(new_nums)-1):
            if new_nums[j] > new_nums[j-1] and new_nums[j] > new_nums[j+1]:
                answer += 1
            pass
            if new_nums[j] < new_nums[j-1] and new_nums[j] < new_nums[j+1]:
                answer += 1
            pass
        return answer
        
