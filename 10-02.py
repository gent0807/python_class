from tkinter import Tk, Label, Entry, Button

win= Tk()
win.title('여러위젯구성')

lb=Label(win, text="레이블(Label")
lb.pack()

content=Entry(win)
content.insert(0, '엔트리(Entry')
content.pack()

btn=Button(win, text='OK')
btn.pack()

win.mainloop()