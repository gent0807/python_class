from tkinter import *

class Join:

    def __init__(self):
        self.win=Tk()
        self.win.geometry('400x400')
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

        self.text = StringVar(value=' ')
        self.result=Label(self.win, width=20, textvariable=self.text)
        self.result.grid(row=3, column=1)
        self.win.mainloop()
    def update(self):
        uid=self.et1.get().strip()
        pwd=self.et2.get().strip()
        if uid in usersdata.keys():
            self.text.set("이미 존재하는 아이디입니다. 다시 입력하세요.")
        else:
            usersdata[uid]=pwd
            self.text.set("가입이 완료되었습니다.")
    def close(self):
        self.win.destroy()


def openJoinPage():
    Join()
def checkid():
    uid = et1.get().strip()
    pwd = et2.get().strip()
    if uid in usersdata.keys():
        '''if pwd==usersdata[uid]:
        
        '''

    else:
        sentence.set('등록된 아이디가 아닙니다.')

usersdata={}


loginPage=Tk()
loginPage.geometry('400x400')
loginPage.title("로그인")

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
loginResult=Label(loginPage, width=20, textvariable=sentence)
loginResult.grid(row=3,column=1)


loginPage.mainloop()