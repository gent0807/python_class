sports =['축구', '야구', '농구', '배구']
sports.insert(1,11)
sports.insert(3,9)
sports.insert(5,5)
sports.insert(7,6)
print('메소드 insert()로 팀원 수 삽입')
print(sports); print()
sports= ['축구', '야구', '농구', '배구']
for i in range(1,len(sports)*2,2):
 sports.insert(i,'')
print("메소드 insert()로 '' 삽입")
print(sports); print()

num=[11, 9, 5, 6]
sports[1::2]=num
print("슬라이스 sports[1::2]에 num을 대입")
print(sports); print()