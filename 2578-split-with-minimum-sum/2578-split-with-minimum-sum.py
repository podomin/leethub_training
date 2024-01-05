class Solution:
    def splitNum(self, num: int) -> int:
        num_str = sorted(str(num))
        num_1 = ""
        num_2 = ""
        for i, c in enumerate(num_str):
            if i % 2 == 0:
                num_1 += c
            else:
                num_2 += c
        return int(num_1) + int(num_2)
     
    
        