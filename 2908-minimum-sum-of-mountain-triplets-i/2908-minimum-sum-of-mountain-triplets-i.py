class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        candidate = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        cur_sum = nums[i] + nums[j] + nums[k]
                        print(i, j, k, cur_sum)
                        candidate.append(cur_sum)
        if not candidate:
            return -1                
        return min(candidate)
        


        