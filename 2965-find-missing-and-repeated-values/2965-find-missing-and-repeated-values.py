class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from collections import Counter
        n = len(grid)
        answer = [-1, -1]
        c = Counter()
        for i in range(n):
            for j in range(n):
                c[grid[i][j]] += 1
        print(c)
        # 1부터 n까지 숫자들 중에서
        # 2번 등장하는 숫자는, answer[0]
        # 0번 등장하는 숫자는, answer[1]
        for i in range(1, n*n+1):
            if c[i] == 2:
                answer[0] = i
            elif c[i] == 0:
                answer[1] = i
        return answer
        