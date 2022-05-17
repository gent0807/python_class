from tkinter import *

users=dict(python='power', java='beauty')

def checkid():
    uid=et1.get().strip()
    pwd=et2.get().strip()
    print(uid, pwd)
    if uid in users.keys():
        if users[uid]==pwd:
            print('로그인 성공')
        else:
            print('암호를 확인하세요.')
    else:
        print('사용자 이름을 확인하세요')
win=Tk()
win.title('사용자 인증')

lb1=Label(win, text='사용자 이름')
lb2=Label(win, text='암호')
