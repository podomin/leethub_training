class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        answer = sorted(nums)
        # 앞뒤앞뒤 순서 바꿔주기
        for i in range(0, len(nums), 2):
            tmp = answer[i]
            answer[i] = answer[i+1]
            answer[i+1] = tmp
            
        return answer
        