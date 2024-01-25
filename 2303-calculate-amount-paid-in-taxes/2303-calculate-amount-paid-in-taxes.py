class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for upper, percent in brackets:
            if upper <= income:
                amount = upper - prev
                answer += round(amount * percent / 100, 5)
                prev = upper
            else:
                amount = income - prev
                answer += round(amount * percent / 100, 5)
                break
        return answer

        