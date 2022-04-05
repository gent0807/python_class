from random import randint
lst=[]
for _ in range(9):
    lst.append(randint(1,99))

print('리스트', lst)
print('정렬 리스트', sorted(lst))
print('역순 리스트', sorted(lst,reverse=True))