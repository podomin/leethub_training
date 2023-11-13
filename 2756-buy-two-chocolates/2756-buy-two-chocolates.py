class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # 1. 가격이 가장 낮은 초콜렛 2개의 합 구하기
        # 2. 내가 가진 돈과 크기 비교하기
        # 3-1. 살 수 있으면 사고 나서 금액 리턴하기
        # 3-2. 살 수 없으면 돈 그래도 리턴하기
        chocolate = sum(sorted(prices)[:2])
        if chocolate <= money:
            return money - chocolate
        return money

        

        