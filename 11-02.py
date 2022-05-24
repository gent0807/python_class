lst=['C/C++', 'java', 'c#', 'python']

try:
    print(lst[3])
except Exeption as e:
    print('예외 발생 이름:{}'.format(type(e)))
    print('예외 발생 이유:{}'.format(e))
else:
    print('잘 실행했습니다.')
finally:
    print('예외 처리가 잘되는군요!')
