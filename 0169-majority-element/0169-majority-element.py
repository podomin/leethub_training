

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        # 1. 숫자별로 등장하는 빈도수 계산하기
        # 2. 반복문을 돌면서 과반수 이상인지 체크하기
        # 3. 과반수 이상 등장했다면 해당 숫자 리턴하기
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1
        for number, count in count_dict.items():
            if count > len(nums) // 2:
                return number

