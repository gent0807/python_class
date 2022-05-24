import math
try:
    n=int(input('양의 정수 입력>>'))
    if n<=0:
        raise Exception('양의 정수르 입력하세요.')
except ValueError as exp:
    print()

except Exception as e:
    print()
else:
    print('{}!={}'.format(n, math.factorial(n)))

finally:
    print()