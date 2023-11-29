class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for i in range(low, high+1):
            num_str = str(i)
            # 길이가 홀수일 때에는 continue
            if len(num_str) % 2 ==1:
                continue

            # head의 각 자리 숫자의 합
            # tail의 각 자리 숫자의 
            head = num_str[:len(num_str) // 2]
            tail = num_str[len(num_str) // 2:]
            # 두 합이 같으면 answer +=
            if sum([int(c) for c in head]) == sum([int(c) for c in tail]):
                answer += 1
        return answer

            
        