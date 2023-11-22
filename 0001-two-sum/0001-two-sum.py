class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        for key in d:
            diff = target - key
            if diff not in d:
                continue
            if diff == key:
                if len(d[diff]) == 2:
                    return d[diff]
            else:
                return d[diff] + d[key]

        