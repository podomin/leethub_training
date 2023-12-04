class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print("l", l, "r", r, "mid", mid)
            # up down 게임에서 정답을 떄려맞춘 경우
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return answer