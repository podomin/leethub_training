answer = [0,0]
for i, row in enumerate(mat):
one_cnt = row.count(1)
# print(row, one_cnt)
if answer[1] < one_cnt:
answer = (i, one_cnt)
answer[0] = i
answer[1] = one_cnt
# answer[1] 보다 one_cnt가 크다면
# answer에 (i, one_cnt)를 할당
return answer
​