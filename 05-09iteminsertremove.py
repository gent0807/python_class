item= ['연필', '볼펜']
# 현재 학용품 품목 출력
print(item)

# 연필 1개와 볼펜 세 자루 삽입
item.insert(1,2)
item.insert(3,3)
# 맨 뒤에 지우개, 1개 삽입
item.insert(4, '지우개')
item.insert(5, 1)

print(item.pop(1))
item.remove('연필')
del item[2:]
