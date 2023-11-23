class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        print(set1, set2, set3)
        print((set1 & set2) | (set2 & set3) | (set1 & set3))
        answer = list((set1 & set2) | (set2 & set3) | (set1 & set3))

        return answer
        