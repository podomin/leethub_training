class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for k, value in c.items():
            # value가 짝수 체크
            # 짝수가 아니라면 false
            if value % 2 != 0:
                return False
        return True
            
            

        