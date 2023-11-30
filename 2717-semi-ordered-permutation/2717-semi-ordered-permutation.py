class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        answer = 0
        length = len(nums)
        first_index = nums.index(1)
        last_index = nums.index(length)
        print(first_index, last_index)
        # 1은 맨 앞으로 가야함
        # 즉, 현재 인덱스 만큼 앞으로 이동하면 됨
        # n은 맨 뒤로 가야함
        # 즉, 배열 전체 길이에서 현재 인덱스만큼 빼주면 됨
        # 이 때, 1이 n보다 뒤에 있으면, 연산을 한 번 더 적게 하면 됨
        if first_index > last_index:
            return first_index + (len(nums) - last_index -1) -1
        else:
            return first_index + (len(nums) - last_index -1)



        