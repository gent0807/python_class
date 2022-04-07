from random import choice
dcs = {'가위': '보오', '바위': '가위', '보오': '바위'}
tit = ['비김', '철수', '영희', '승자']
rsp = ('가위', '바위', '보오')
cnt = {tit[0]: 0, tit[1]: 0, tit[2]: 0}

print('*' * 20)
print('{:4} {:4} {:^5}'.format(tit[1], tit[2], tit[3]))
print('*' * 20)

numgame = 20
for _ in range(numgame):

    cs = choice(rsp)

    yh = choice(rsp)


    print('{:4} {:4}'.format(cs, yh), end=' ')


    if cs == yh:
        index = 0

    elif dcs[cs] == yh:
        index = 1

    else:
        index = 2
    cnt[tit[index]] += 1
    print('{:3}{}'.format(tit[index], cnt[tit[index]]))
print()
print('총 게임 회수: %d  비긴 회수: %d' % (numgame, cnt[tit[0]]))

vgame = cnt[tit[1]] + cnt[tit[2]]
print('철수 승률: {:.2f}'.format(cnt[tit[1]] / vgame))
print('영희 승률: {:.2f}'.format(cnt[tit[2]] / vgame))