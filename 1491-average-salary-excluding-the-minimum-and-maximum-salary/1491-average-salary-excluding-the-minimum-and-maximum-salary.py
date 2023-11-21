class Solution:
    def average(self, salary: List[int]) -> float:
        answer=[]
        low = min(salary) 
        great = max(salary)
        for num in salary:
            if num != low and num!= great:
                answer.append(num)
        return sum(answer)/len(answer)
        