class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 1. 현재 candies에서 가장 큰 값 찾기
        # 2. for 문을 돌면서 현재 candy 개수와 extraCandies 합쳐주기
        # 3. 합친 값이 가장 큰 값보다 크다면 True, 아니면 False를 answer에 추가하기
        answer = []
        maxnum = max(candies)
        for candy in candies:
            added_candy = candy + extraCandies
            print(added_candy, maxnum)
            if added_candy >= maxnum:
                answer.append(True)
            else:
                answer.append(False)
        return answer