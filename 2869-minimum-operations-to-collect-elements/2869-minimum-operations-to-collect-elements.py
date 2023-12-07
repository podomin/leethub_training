class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
      # set.issubset
      collection = set()
      target = set([x+1 for x in range(k)])
      print(target)
      for i in range(len(nums)):
        collection.add(nums[len(nums) -1 -i])
        print(collection)
        if target.issubset(collection):
          return i + 1



      
        