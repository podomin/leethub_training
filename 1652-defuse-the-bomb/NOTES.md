hint
​
% len(code -> 범위를 넘칠 수 있으니까
​
class Solution:
def decrypt(self, code: List[int], k: int) -> List[int]:
answer = []
if k > 0:
for i in range(len(code)):
cur_sum = 0
for j in range(k):
#print(code[i], code[(i+j+1) % len(code)])
cur_sum += code[(i+j+1) % len(code)]
answer.append(cur_sum)
elif k < 0:
for i in range(len(code)):
cur_sum = 0
for j in range(abs(k)):
#print(code[i], code[(i+j-abs(k)) % len(code)])
cur_sum += code[(i+j-abs(k)) % len(code)]
answer.append(cur_sum)
elif k == 0:
for i in range(len(code)):
answer.append(0)
return answer