prev 변수
​
answer = []
prev = 0
for upper, percent in brackets:
amount = upper - prev
prev = upper
if upper > income:
amount -= upper - income
if income == 0 or amount < 0:
amount = 0
#print(amount,  (amount * percent / 100), prev)
# 내 소득과 비교해서 넘어서는 부분은 세금 내지 않도록
answer.append(amount * percent / 100)
return sum(answer)