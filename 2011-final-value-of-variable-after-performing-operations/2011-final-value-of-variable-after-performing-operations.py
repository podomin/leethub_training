class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for x in operations:
            print(x)
            if x == "--X" or x == "X--":
                answer -= 1
            else:
                answer += 1    
        return answer
        