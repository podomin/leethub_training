class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        answer = []
        c = Counter(nums)
        print(c)
        sort_nums =  sorted(nums, key=lambda x: (c[x], -x))  
        return sort_nums

        