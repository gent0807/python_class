stocks = { '삼성에스디에스': 242000, '삼성전자': 47000 }
stocks['엔씨소프트'] = 52600
stocks['핸디소프트'] = 5120
stocks.update(dict(골프존=215000, 기아=56300))
print(stocks)
while True:
    which = input("주식 이름 ? ")
    if which in stocks:
        print('{}: {}'.format(which, stocks[which]))
    else:
        print('주식 이름이 없습니다.')
        break