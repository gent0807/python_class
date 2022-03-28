menu = '''Coffee menu!
        1.아메리카노    2000
        2.카페라테      2500
        3.카푸치노      3000
        4.캐러멜마끼아또 4000
        0. 주문 종료
    종류?'''

print('환영합니다. 음료를 선택하세요.')
total = 0
while True:
    order=int(input(menu))
    if