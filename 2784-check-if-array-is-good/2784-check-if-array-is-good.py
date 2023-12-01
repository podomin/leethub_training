class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        from collections import Counter
        c = Counter(nums)
        answer = True
        for i in range(1, len(nums)):
            if i != len(nums) -1:
                if c[i] != 1:
                    answer = False
                    break
            else:
                if c[i] != 2:
                    answer = False
                    break

        return answer


        
        