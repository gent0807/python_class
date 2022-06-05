def hello(names):
    for each in names:
        print('안녕 , {}!'.format(each))
def  mykeyprint(a):
    for key in a:
        print('{}: {}'.format(key,a[key]), end=' ')
    print()

mycar={'brand':'현대', 'model':'제네시스', 'year':2016}#

hello(['방탄소년단', '여자친구'])
mykeyprint(mycar)

