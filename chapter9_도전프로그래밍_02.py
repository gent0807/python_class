from math import factorial as fact
from statistics import median, mean, variance, stdev

if __name__=='__main__':
    for i in range(1, 21, 5):
        print('{:2d}!={}'.format(i,fact(i)))

    st=[80, 99, 77, 65, 92, 74, 82]
    print()
    print(st)
    print('중앙값:%.2f' % median(st))
    print('평균:%.2f' % mean(st))
    print('분산:%.2f' % variance(st))
    print('표쥰편차:%.2f' % stdev(st))
