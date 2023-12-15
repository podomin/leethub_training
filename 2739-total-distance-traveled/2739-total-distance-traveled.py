class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        answer = 0
        while mainTank >= 5 and additionalTank > 0:
            # 5 리터 소진하고 1리터 채우기
            mainTank -= 4
            additionalTank -= 1
            # 이때 50km 만큼 이동
            answer += 50 
        # 남은 mainTank모두 사용해서 이동
        answer += mainTank * 10
        return answer
        