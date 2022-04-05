from random import randint
lst=[]
for _ in range(10):
    lst.append(randint(1, 99))
print('리스트: ', lst)

tup = tuple(lst)
print('튜플: ', tup)
print('튜플 정렬된 리스트: ', sorted(tup))
print()

print('합: %d, 항목수:%d ' % (sum(tup), len(tup)))
print('최대 %d, 최소 : %d, 평균:%.2f' % (max(tup),min(tup), sum(tup)/len(tup)))