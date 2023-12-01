class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            print(start, end)
            for i in range(start, end+1):
                print(i)
                covered.add(i)
        return len(covered)