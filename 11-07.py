f=open('pyzen.txt','r')

while True:
    line=f.readline()
    if not line:
        break
    print(line, end='')
f.close()