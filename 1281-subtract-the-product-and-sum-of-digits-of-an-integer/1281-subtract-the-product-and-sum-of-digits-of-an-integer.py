class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_digit = 1
        sum_digit = 0
        for c in str(n):
            sum_digit += int(c)
            product_digit *= int(c)
        return product_digit - sum_digit

        