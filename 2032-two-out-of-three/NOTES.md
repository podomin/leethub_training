교집합      print(set2 & set3)
합집합      print(set2 | set3)
​
set1 = set(nums1)
set2 = set(nums2)
set3 = set(nums3)
print(set1, set2, set3)
print((set1 & set2) | (set2 & set3) | (set1 & set3))
answer = list((set1 & set2) | (set2 & set3) | (set1 & set3))
​
return answer