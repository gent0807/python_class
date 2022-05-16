import turtle as t
from random import randint

tshs = ['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']
han = ['화살', '원', '거북이', '사각형', '삼각형', '전통']
cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
        'gray', 'yellow', 'cyan', 'orange', 'aqua']
t.setup(800, 500)
t.clear()
for i in range(20):
    t.penup()
    x = randint(-300, 300)
    y = randint(-200, 200)
    t.setpos(x, y)

    t.pendown()
    t.shape(tshs[i % len(tshs)])
    t.fillcolor(cols[i % len(cols)])
    t.begin_fill()
    t.circle(randint(3, 50))
    t.end_fill()
    # 현재 위치에서 글쓰기
    t.pensize(2)
    t.pencolor(cols[(i + 1) % len(cols)])
    t.write(han[i % len(han)])