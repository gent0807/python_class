import turtle as t
colors=['yellow', 'red', 'blue']
t.setup(500, 500)
t.bgcolor('black')
t.speed(0)
for i in range(200):
    t.color(colors[i%len(colors)])
    t.width(i/200+1)
    t.forward(i*2)
    t.left(119)