class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        # 1. 주어진 리스트에서 서로 다른 숫자 2개로 이루어진 쌍 찾기
        # 2. 두 수의 합이 target 보다 작은지 검사하기
        # 3. target 보다 작으면 answer에 1 더해주기

        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(i,j)
                if nums[i] + nums[j] < target:
                    answer += 1
        return answer


