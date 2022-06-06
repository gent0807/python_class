from tkinter import *
import pygame
class ChessGame:
    def __init__(self):
        self.page=Tk()
        self.page.title('Chess Game')
        self.page.geometry('1000x800+220+30')

        self.block=list()

        for i in range(8):
            for j in range(8):
                if(i%2==0 and j%2==0):
                    self.lb=Label(self.page, width=13, height=6, bg='grey')
                    self.lb.grid(row=i, column=j, sticky=E)
                    list[i].append(self.lb)
                elif(i%2==0 and j%2==1):
                    self.lb = Label(self.page, width=13, height=6, bg='yellow')
                    self.lb.grid(row=i, column=j, sticky=E)
                    list[i].append(self.lb)
                elif(i%2==1 and j%2==0):
                    self.lb = Label(self.page, width=13, height=6, bg='yellow')
                    self.lb.grid(row=i, column=j, sticky=E)
                    list[i].append(self.lb)
                elif(i%2==1, j%2==1):
                    self.lb = Label(self.page, width=13, height=6, bg='grey')
                    self.lb.grid(row=i, column=j, sticky=E)
                    list[i].append(self.lb)




        self.page.mainloop()
class Join:

    def __init__(self):
        self.win=Tk()
        self.win.title('회원가입')
        self.win.geometry('400x400+550+220')
        self.win.config(bg='beige')
        self.lb1=Label(self.win, text='ID')
        self.lb2=Label(self.win, text='PW')
        self.lb1.grid(row=0, column=0, sticky=E)
        self.lb2.grid(row=1, column=0, sticky=E)

        self.et1=Entry(self.win)
        self.et2=Entry(self.win)
        self.et1.grid(row=0, column=1)
        self.et2.grid(row=1, column=1)

        self.lb=Label(self.win)
        self.lb.grid(row=2, column=0, columnspan=2)

        self.btn1=Button(self.lb, text='확인', command=self.update)
        self.btn2 =Button(self.lb, text='닫기', command=self.close)
        self.btn1.grid(row=0, column=0, padx=10)
        self.btn2.grid(row=0, column=1, padx=10)


        self.comment=StringVar(value=' ')
        self.text='기등록 아이디 혹은 빈칸이면 확인 눌러도 창 안 닫힘'
        self.result=Label(self.win, width=40, text=self.text, textvariable=self.comment)
        self.result.grid(row=3, column=1)
        self.win.mainloop()

    def update(self):
        uid=self.et1.get().strip()
        pwd=self.et2.get().strip()
        if uid in usersdata.keys():
            self.comment.set('이미 존재하는 아이디입니다. 다시 입력하세요.')
        else:
            if(uid==''):
                self.comment.set('빈칸입니다. 아이디를 입력하세요.')
            else:
                usersdata[uid]=pwd
                self.comment.set('가입이 완료되었습니다.')
                self.win.destroy()
    def close(self):
        self.txt=''
        self.win.destroy()


def openJoinPage():
    sentence.set(' ')
    Join()

def checkid():
    uid = et1.get().strip()
    pwd = et2.get().strip()
    if uid in usersdata.keys():
        sentence.set(' ')
        if pwd==usersdata[uid]:
            sentence.set('contact')
            ChessGame()
        else:
            sentence.set('암호를 확인하세요.')

    else:
        if(uid==''):
            sentence.set('빈칸입니다. 아이디를 입력하세요.')
        else:
            sentence.set('등록된 아이디가 아닙니다.')



usersdata={}

loginPage=Tk()
loginPage.geometry('400x400+520+250')
loginPage.title("로그인")
loginPage.config(bg='beige')

lb1=Label(loginPage, text='ID')
lb2=Label(loginPage, text='PW')
lb1.grid(row=0, column=0, sticky=E)
lb2.grid(row=1, column=0, sticky=E)


et1=Entry(loginPage)
et2=Entry(loginPage)
et1.grid(row=0, column=1)
et2.grid(row=1, column=1)

lb=Label(loginPage)
lb.grid(row=2,column=0,columnspan=2)
bt1=Button(lb, text='회원가입', command=openJoinPage)
bt2=Button(lb, text='로그인', command=checkid)
bt1.grid(row=0, column=0, padx=10)
bt2.grid(row=0, column=1, padx=10)

sentence=StringVar(value=' ')
loginResult=Label(loginPage, width=25, textvariable=sentence)
loginResult.grid(row=3,column=1)


loginPage.mainloop()