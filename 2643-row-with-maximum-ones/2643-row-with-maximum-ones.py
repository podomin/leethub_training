class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0,0]
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            if answer[1] < one_cnt:
                answer = (i, one_cnt)
        return answer



        