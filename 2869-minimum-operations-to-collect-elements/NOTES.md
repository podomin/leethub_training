list comprehension 검색...
target = set([x+1 for x in range(k)])
​
​
이거 어떻게 역순이지...원리 검색?
nums[len(nums) -1 -i]
​
collection = []
target = set([x+1 for x in range(k)])
print(target)
for i in range(len(nums)):
collection.append(nums[len(nums) -1 -i])
print(collection)
if target.issubset(collection):
return len(collection)