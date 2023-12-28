answer = []
sort_nums = sorted(nums)
for i in range(0,len(sort_nums),2):
answer.append(sort_nums[i+1])
answer.append(sort_nums[i])
return answer
코치님 풀이
answer = sorted(nums)
앞뒤 앞뒤 순서 바꿔주기
​
answer = []
nums = sorted(nums)
while nums:
min_a = min(nums)
nums.remove(min_a)
min_b = min(nums)
nums.remove(min_b)
​
answer.append(min_b)
answer.append(min_a)
return answer