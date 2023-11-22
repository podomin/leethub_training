for i in range(len(nums)):
for j in range(i+1, len(nums)):
print(nums[i],nums[j])
if nums[i] + nums[j] == target:
return [i,j]
​
더 어려운 버전
​
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
from collections import defaultdict
​
d = defaultdict(list)
for i, num in enumerate(nums):
d[num].append(i)
for key in d:
diff = target - key
if diff not in d:
continue
if diff == key:
if len(d[diff]) == 2:
return d[diff]
else:
return d[diff] + d[key]