from math import pi
import random

p=round(pi, 4)
r=round(random.random()*10, 2)

def getarea(r):
    area=p*r*r
    return area

print('원의 반지름: ', r)
print('원주율 pi: ', p)
print('반지름이', r, '인 원의 면적은 ',  round(getarea(r), 2))
