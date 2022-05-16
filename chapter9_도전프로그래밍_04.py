import turtle as t
t.setup(500, 400)

rep=60
t.speed(0)

for i in range(rep):
    for i in range(5):
        t.forward(100)
        t.left(360/5)
    t.left(360/rep)