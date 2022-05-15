from random import sample
from random import randint

rank={6: ('1등', 1000000000),
      5: {1:('2등',5000000),
          0:('3등',1000000)},
      4:('4등', 50000),
      3: ('5등', 5000)
    }
def makenum(same):
    nums=winnum.copy()
    for i in range(6-same):
        nums.pop()

    while len(nums) !=6:
        n= randint(1,45)
        if n not in winnum:
            nums.add(n)
    return nums
def getwinner(lotto):
    global bonus
    for i, item in enumerate(lotto):
        print("%c" % (ord('A')+ i), end= ' ')
        win= winnum.intersection(item)
        if win:
            wincnt= len(win)
            print('당첨 번호 개수 %d, ' % wincnt, end= '')
            printnums(win)
            if 3<=wincnt:
                grade= rank[wincnt]
                if 5== wincnt:
                    if bonus in item:
                        print('\t 보너스 번호 %d도 맞추!!' % bonus)
                        grade=rank[wincnt][1]
                    else:
                        grade=rank[wincnt][0]
                print('\t%s %s원' % (grade[0], grade[1]))
            else:
                print('\t 2개 이하 맞춰, 꽝!')
        else:
            print('모두 꽝!!')
def printlotto(lotto):
    for i, items in enumerate(lotto):
        print('%c 자동' % (ord('A')+i), end= ' ')
        printnums(items)
    print()

def printnums(nums):
    for num in sorted(nums):
        print('%02d' % num, end= ' ')
    print()

winnum=set(sample( list(range(1, 46)), 7))
bonus= winnum.pop()
print('당첨 번호: ', end= '')
printnums(winnum)
print('보너스 번호:', bonus)
print()

lottos=[]
rank1num=winnum.copy()
lottos.append(rank1num)

rank2num=winnum.copy()
rank2num.pop(); rank2num.add(bonus)
lottos.append(rank2num)

rank3num= winnum.copy()
rank3num.pop()

while True:
    num= randint(1, 45)
    if num != bonus and num not in rank3num:
        rank3num.add(num)
        break
lottos.append(rank3num)

for i in range(5):
    lottos.append(makenum(4-i))

printlotto(lottos)

getwinner(lottos)