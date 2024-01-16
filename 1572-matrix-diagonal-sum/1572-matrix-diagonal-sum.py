class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        answer = 0
        for i in range(n):
            print(mat[i][i], mat[i][n-i-1])
            answer += mat[i][i]
            answer += mat[i][n-i-1]
        if n % 2 == 1:
            mid = n // 2
            answer -= mat[mid][mid]
        return answer