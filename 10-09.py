from tkinter import *
win=Tk()
win.title("레이블 그림 로드")

img=PhotiImage(file='C:\\이미테이션 게임.png')
lbimg=Label(win, image=img)
lbimg.pack()

win.mainloop()