class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        answer = []
        print (c)
        for key in c:
            if c[key] > len(nums)/3:
                answer.append(key)
            else:
                pass
        return answer
        