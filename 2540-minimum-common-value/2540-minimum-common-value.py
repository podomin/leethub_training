class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(set(nums2))
        if common:
            return min(common)
        else:
            return -1



        