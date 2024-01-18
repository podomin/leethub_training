class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        answer = 0
        for i in range(len(nums) - k + 1):
            int_n = nums[i:i+k]
            print(int_n)
            if int(int_n) == 0:
                pass
            elif num % int(int_n) == 0:
                answer += 1
             
        return answer
        