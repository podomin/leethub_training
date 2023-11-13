class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # for문 이용해서 각 사람별 총액 계산, , sum
        # answer와 비교해서 더 큰 값을 answer로 지정, max
        answer = 0
        for money in accounts:
            answer =  max(sum(money), answer)
        return answer
            
                





        
        
        
        


