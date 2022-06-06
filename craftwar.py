import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import operator

import pygame
from tkinter import *

class join:

    def __init__(self):
        self.win=Tk()
        self.win.title('회원가입')
        self.win.geometry('400x400+550+220')
        self.win.config(bg='beige')

        self.firstLabel=Label(self.win)
        self.firstLabel.pack()
        self.secondLabel=Label(self.win)
        self.secondLabel.pack()

        self.lb1=Label(self.firstLabel, text='ID')
        self.lb2=Label(self.secondLabel, text='PW')
        self.lb1.grid(row=0, column=0, sticky=E)
        self.lb2.grid(row=0, column=0, sticky=E)

        self.et1=Entry(self.firstLabel)
        self.et2=Entry(self.secondLabel)
        self.et1.grid(row=0, column=1)
        self.et2.grid(row=0, column=1)

        self.lb=Label(self.win)
        self.lb.pack()

        self.btn1=Button(self.lb, text='확인', command=self.update)
        self.btn2 =Button(self.lb, text='닫기', command=self.close)
        self.btn1.grid(row=0, column=0, padx=10)
        self.btn2.grid(row=0, column=1, padx=10)



        self.text='기등록 아이디 혹은 빈칸이면 확인 눌러도 창 안 닫힘'
        self.result=Label(self.win, width=40, text=self.text)
        self.result.pack()
        self.win.mainloop()

    def update(self):
        uid=self.et1.get().strip()
        pwd=self.et2.get().strip()
        if uid not in usersdata.keys() and uid!='':
            usersdata[uid] = pwd
            self.win.destroy()
    def close(self):
        self.txt=''
        self.win.destroy()


def openjoinpage():
    sentence.set(' ')
    join()

def checkid():
    uid = et1.get().strip()
    pwd = et2.get().strip()
    if uid in usersdata.keys():
        sentence.set(' ')
        if pwd==usersdata[uid]:
            sentence.set('contact')

            pygame.init()
            pygame.mixer.init()


            size = [800, 900]
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('GAME')

            shot = pygame.mixer.Sound("E:/shot.wav")
            shot.set_volume(0.1)
            explosion=pygame.mixer.Sound("E:/explosion.wav")
            explosion.set_volume(0.1)

            clock = pygame.time.Clock()
            black=(0,0,0)
            color=black

            #획득 결과 관여
            count=0
            energy=100
            hit=0
            score=0
            start_time = datetime.now()
            new_start_time=datetime.now()

            #분기 결정
            k=0

            #flag 변수들
            lmove = False
            rmove = False
            upmove = False
            downmove = False
            missilefire=False
            bombfire=False
            GAMEOVER=False
            clearpossible = False

            done=False

            #캐릭터 인스턴스들의 공통 속성을 반영한 클래스 작성
            class thing:
                def __init__(self):
                    self.x=0
                    self.y=0
                    self.transfer=0
                def insert_img(self, adrress, x_size, y_size):
                    if(adrress[-3:0]=='png'):
                        self.img= pygame.image.load(adrress).convert_alpha()
                    else:
                        self.img = pygame.image.load(adrress)
                    self.img=pygame.transform.scale(self.img,(x_size,y_size))
                    self.sx, self.sy=self.img.get_size()
                def show(self):
                    screen.blit(self.img,(self.x, self.y))

            class ball(thing):
                def __init__(self):
                    super().__init__()
                    self.xtransfer=random.randint(-4,4)
                    self.ytransfer=random.randint(-4,4)


            def crash(a,b):
                if(a.x-b.sx<=b.x) and (b.x<=a.x+a.sx):
                    if(a.y-b.sy<=b.y)and(b.y<=a.y+a.sy):
                        return True
                    else:
                        return False
                else:
                    return False



            #default 인스턴스를 생성하여 속성 설정
            craft=thing()
            craft.insert_img("E:/craft.png", 50, 80)
            craft.x=round(size[0]/2-craft.sx/2)
            craft.y=size[1]-craft.sy-15
            craft.transfer=5

            missiles=list()
            bomb1s=list()
            bomb2s= list()
            bomb3s= list()
            bomb4s= list()
            negativeballs=list()
            positiveballs=list()

            while done == False:

                clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            done=True

                screen.fill(color)
                font=pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 15)
                text = font.render("PRESS SPACE KEY TO START THE GAME", True, (255, 255, 255))
                screen.blit(text, (225, round(size[1]/2-50)))

                pygame.display.flip()

            done=False
            while done == False:

                clock.tick(60)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_LEFT:
                            lmove=True
                        elif event.key==pygame.K_RIGHT:
                            rmove=True
                        elif event.key==pygame.K_UP:
                            upmove=True
                        elif event.key==pygame.K_DOWN:
                            downmove=True
                        elif event.key==pygame.K_SPACE:
                            missilefire=True
                            k=0
                        elif event.key==pygame.K_a:
                            bomb1=thing()
                            shot.play()
                            count+=1
                            bomb1.insert_img("E:/bomb.png", 14, 14)
                            bomb1.x = craft.x
                            bomb1.y = craft.y+craft.sy/2-bomb1.sy/2
                            bomb1.transfer = 10
                            bomb1s.append(bomb1)
                        elif event.key==pygame.K_s:
                            bomb2=thing()
                            shot.play()
                            count += 1
                            bomb2.insert_img("E:/bomb.png", 14, 14)
                            bomb2.x = craft.x
                            bomb2.y = craft.y+craft.sy-bomb2.sy/2
                            bomb2.transfer = 10
                            bomb2s.append(bomb2)
                        elif event.key==pygame.K_d:
                            bomb3=thing()
                            shot.play()
                            count += 1
                            bomb3.insert_img("E:/bomb.png", 14, 14)
                            bomb3.x = craft.x+craft.sx-bomb3.sx/2
                            bomb3.y = craft.y+craft.sy-bomb3.sy/2
                            bomb3.transfer = 10
                            bomb3s.append(bomb3)
                        elif event.key==pygame.K_f:
                            bomb4=thing()
                            shot.play()
                            count += 1
                            bomb4.insert_img("E:/bomb.png", 14, 14)
                            bomb4.x = craft.x+craft.sx-bomb4.sx/2
                            bomb4.y = craft.y+craft.sy/2-bomb4.sy/2
                            bomb4.transfer = 10
                            bomb4s.append(bomb4)
                        elif event.key == pygame.K_r:
                            if clearpossible:
                                negativeballs=list()
                                positiveballs=list()
                                new_start_time=datetime.now()
                    elif event.type==pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            lmove = False
                        elif event.key == pygame.K_RIGHT:
                            rmove = False
                        elif event.key == pygame.K_UP:
                            upmove = False
                        elif event.key == pygame.K_DOWN:
                            downmove = False
                        elif event.key==pygame.K_SPACE:
                            missilefire=False

                now_time = datetime.now()
                delta_time=round((now_time-start_time).total_seconds())
                another_delta_time=round((now_time-new_start_time).total_seconds())
                if another_delta_time>=25:
                    clearpossible=True
                elif another_delta_time<25:
                    clearpossible=False

                if lmove==True:
                    craft.x-=craft.transfer
                    if(craft.x<=0):
                        craft.x=0
                if rmove==True:
                    craft.x+=craft.transfer
                    if(craft.x>=size[0]-craft.sx):
                        craft.x=size[0]-craft.sx
                if upmove==True:
                    craft.y-=craft.transfer
                    if(craft.y<=0):
                        craft.y=0
                if downmove==True:
                    craft.y+=craft.transfer
                    if(craft.y>=size[1]-craft.sy):
                        craft.y=size[1]-craft.sy

                if missilefire==True:
                    if k%5==0:
                        missile=thing()
                        shot.play()
                        count+=1
                        missile.insert_img("E:/missile.jpg", 6, 15)
                        missile.x = round(craft.x+craft.sx/2-missile.sx/2)
                        missile.y = craft.y-missile.sy
                        missile.transfer = 12
                        missiles.append(missile)
                k+=1

                if random.random()>0.98:
                    negativeball=ball()
                    negativeball.insert_img("E:/nball.png",20,20)
                    negativeball.x=random.randrange(0,size[0]-negativeball.sx)
                    negativeball.y= random.randrange(0, size[1]-negativeball.sy)
                    negativeballs.append(negativeball)

                if random.random()>0.98:
                    positiveball = ball()
                    positiveball.insert_img("E:/pball.png", 20, 20)
                    positiveball.x = random.randrange(0, size[0] - positiveball.sx)
                    positiveball.y = random.randrange(0, size[1] - positiveball.sy)
                    positiveballs.append(positiveball)


                garbageindex=list()
                bomb1garbage=list()
                bomb2garbage = list()
                bomb3garbage = list()
                bomb4garbage = list()




                for i in range(len(missiles)):
                    m=missiles[i]
                    m.y-=m.transfer
                    if m.y<=-m.sy:
                        garbageindex.append(i)

                for i in range(len(bomb1s)):
                    b=bomb1s[i]
                    b.x-=b.transfer
                    if b.x<=-b.sx:
                        bomb1garbage.append(i)

                for i in range(len(bomb2s)):
                    b=bomb2s[i]
                    b.x-=b.transfer
                    b.y+=b.transfer
                    if b.x<=-b.sx:
                        bomb2garbage.append(i)
                    elif b.y<=-b.sy:
                        bomb2garbage.append(i)

                for i in range(len(bomb3s)):
                    b = bomb3s[i]
                    b.x += b.transfer
                    b.y += b.transfer
                    if b.x >= size[0]+b.sx:
                        bomb3garbage.append(i)
                    elif b.y <= -b.sy:
                        bomb3garbage.append(i)

                for i in range(len(bomb4s)):
                    b = bomb4s[i]
                    b.x += b.transfer
                    if b.x >= size[0]+b.sx:
                        bomb4garbage.append(i)

                for i in range(len(negativeballs)):
                    nb= negativeballs[i]
                    nb.x+=nb.xtransfer
                    nb.y+=nb.ytransfer

                    if nb.x>=size[0]-nb.sx or nb.x<=0:
                        nb.xtransfer*=-1
                    if nb.y>=size[1]-nb.sy or nb.y<=0:
                        nb.ytransfer*=-1

                for i in range(len(negativeballs)):
                    nb= negativeballs[i]
                    nb.x+=nb.xtransfer
                    nb.y+=nb.ytransfer

                    if nb.x>=size[0]-nb.sx or nb.x<=0:
                        nb.xtransfer*=-1
                    if nb.y>=size[1]-nb.sy or nb.y<=0:
                        nb.ytransfer*=-1

                for i in range(len(positiveballs)):
                    pb= positiveballs[i]
                    pb.x+=pb.xtransfer
                    pb.y+=pb.ytransfer

                    if pb.x>=size[0]-pb.sx or pb.x<=0:
                        pb.xtransfer*=-1
                    if pb.y>=size[1]-pb.sy or pb.y<=0:
                        pb.ytransfer*=-1

                for i in garbageindex:
                    del missiles[i]

                for i in bomb1garbage:
                    del bomb1s[i]

                for i in bomb2garbage:
                    del bomb2s[i]

                for i in bomb3garbage:
                    del bomb3s[i]

                for i in bomb4garbage:
                    del bomb4s[i]

                dm_list = list()
                dnb_list = list()
                for i in range(len(missiles)):
                    for j in range(len(negativeballs)):
                        m = missiles[i]
                        nb = negativeballs[j]
                        if crash(m, nb) == True:
                            explosion.play()
                            dm_list.append(i)
                            dnb_list.append(j)
                dm_list=list(set(dm_list))
                dnb_list=list(set(dnb_list))
                for i in dm_list:
                    del missiles[i]
                for i in dnb_list:
                    del negativeballs[i]
                    hit+=1

                dm1_list = list()
                dpb_list = list()
                for i in range(len(missiles)):
                    for j in range(len(positiveballs)):
                        m = missiles[i]
                        pb = positiveballs[j]
                        if crash(m, pb) == True:
                            dm1_list.append(i)
                            dpb_list.append(j)
                dm1_list = list(set(dm1_list))
                dnb_list = list(set(dpb_list))
                for i in dm1_list:
                    del missiles[i]
                for i in dpb_list:
                    del positiveballs[i]


                dnb_craft_list=list()
                for i in range(len(negativeballs)):
                    nb = negativeballs[i]
                    if crash(nb, craft) == True:
                        dnb_craft_list.append(i)
                        energy -= 15
                        if energy < 0:
                            done = True
                            GAMEOVER=True
                for i in dnb_craft_list:
                    del negativeballs[i]

                dpb_craft_list=list()
                for i in range(len(positiveballs)):
                    pb = positiveballs[i]
                    if crash(pb, craft) == True:
                        dpb_craft_list.append(i)
                        energy += 10
                        if energy >= 100:
                            energy = 100
                for i in dpb_craft_list:
                    del positiveballs[i]


                usedbomb1=list()
                dnb_bomb1_list=list()
                for i in range(len(bomb1s)):
                    for j in range(len(negativeballs)):
                        b = bomb1s[i]
                        nb = negativeballs[j]
                        if crash(b, nb) == True:
                            explosion.play()
                            usedbomb1.append(i)
                            dnb_bomb1_list.append(j)
                usedbomb1=list(set(usedbomb1))
                dnb_bomb1_list=list(set(dnb_bomb1_list))
                for i in usedbomb1:
                    del bomb1s[i]
                for i in dnb_bomb1_list:
                    del negativeballs[i]
                    hit += 1

                usedbomb2 = list()
                dnb_bomb2_list = list()
                for i in range(len(bomb2s)):
                    for j in range(len(negativeballs)):
                        b = bomb2s[i]
                        nb = negativeballs[j]
                        if crash(b, nb) == True:
                            explosion.play()
                            usedbomb2.append(i)
                            dnb_bomb2_list.append(j)
                usedbomb2 = list(set(usedbomb2))
                dnb_bomb2_list = list(set(dnb_bomb2_list))
                for i in usedbomb2:
                    del bomb2s[i]
                for i in dnb_bomb2_list:
                    del negativeballs[i]
                    hit += 1

                usedbomb3 = list()
                dnb_bomb3_list = list()
                for i in range(len(bomb3s)):
                    for j in range(len(negativeballs)):
                        b = bomb3s[i]
                        nb = negativeballs[j]
                        if crash(b, nb) == True:
                            explosion.play()
                            usedbomb3.append(i)
                            dnb_bomb3_list.append(j)
                usedbomb3 = list(set(usedbomb3))
                dnb_bomb3_list = list(set(dnb_bomb3_list))
                for i in usedbomb3:
                    del bomb3s[i]
                for i in dnb_bomb3_list:
                    del negativeballs[i]
                    hit += 1

                usedbomb4 = list()
                dnb_bomb4_list = list()
                for i in range(len(bomb4s)):
                    for j in range(len(negativeballs)):
                        b = bomb4s[i]
                        nb = negativeballs[j]
                        if crash(b, nb) == True:
                            explosion.play()
                            usedbomb4.append(i)
                            dnb_bomb4_list.append(j)
                usedbomb4 = list(set(usedbomb4))
                dnb_bomb4_list = list(set(dnb_bomb4_list))
                for i in usedbomb4:
                    del bomb4s[i]
                for i in dnb_bomb4_list:
                    del negativeballs[i]
                    hit += 1

                errorbomb1 = list()
                dpb_bomb1_list = list()
                for i in range(len(bomb1s)):
                    for j in range(len(positiveballs)):
                        b = bomb1s[i]
                        pb = positiveballs[j]
                        if crash(b, pb) == True:
                            errorbomb1.append(i)
                            dpb_bomb1_list.append(j)
                errorbomb1 = list(set(errorbomb1))
                dpb_bomb1_list = list(set(dpb_bomb1_list))
                for i in errorbomb1:
                    del bomb1s[i]
                for i in dpb_bomb1_list:
                    del positiveballs[i]

                errorbomb2 = list()
                dpb_bomb2_list = list()
                for i in range(len(bomb2s)):
                    for j in range(len(positiveballs)):
                        b = bomb2s[i]
                        pb = positiveballs[j]
                        if crash(b, pb) == True:
                            errorbomb2.append(i)
                            dpb_bomb2_list.append(j)
                errorbomb2 = list(set(errorbomb2))
                dpb_bomb2_list = list(set(dpb_bomb2_list))
                for i in errorbomb2:
                    del bomb2s[i]
                for i in dpb_bomb2_list:
                    del positiveballs[i]

                errorbomb3 = list()
                dpb_bomb3_list = list()
                for i in range(len(bomb3s)):
                    for j in range(len(positiveballs)):
                        b = bomb3s[i]
                        pb = positiveballs[j]
                        if crash(b, pb) == True:
                            errorbomb3.append(i)
                            dpb_bomb3_list.append(j)
                errorbomb3 = list(set(errorbomb3))
                dpb_bomb3_list = list(set(dpb_bomb3_list))
                for i in errorbomb3:
                    del bomb3s[i]
                for i in dpb_bomb3_list:
                    del positiveballs[i]

                errorbomb4 = list()
                dpb_bomb4_list = list()
                for i in range(len(bomb4s)):
                    for j in range(len(positiveballs)):
                        b = bomb4s[i]
                        pb = positiveballs[j]
                        if crash(b, pb) == True:
                            errorbomb4.append(i)
                            dpb_bomb4_list.append(j)
                errorbomb4 = list(set(errorbomb4))
                dpb_bomb4_list = list(set(dpb_bomb4_list))
                for i in errorbomb4:
                    del bomb4s[i]
                for i in dpb_bomb4_list:
                    del positiveballs[i]


                screen.fill(color)

                craft.show()

                for m in missiles:
                    m.show()

                for b in bomb1s:
                    b.show()

                for c in bomb2s:
                    c.show()

                for d in bomb3s:
                    d.show()

                for e in bomb4s:
                    e.show()

                for nball in negativeballs:
                    nball.show()

                for pball in positiveballs:
                    pball.show()

                font=pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 20)
                text=font.render("hit target:{}  use weapon:{}".format(hit,count), True, (255,255,0))
                screen.blit(text, (10,5))

                font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 20)
                time_text = font.render("time:{}".format(delta_time), True, (255, 255, 255))
                screen.blit(time_text, (size[0]-90, 5))

                font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 20)
                clear_text = font.render("clearpossible:{}".format(clearpossible), True, (255, 255, 255))
                screen.blit(clear_text, (size[0] - 230, 25))



                pygame.display.flip()

            while GAMEOVER==True:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        GAMEOVER=0


                count//=6
                score=delta_time+hit-count
                if(score<0):
                    score=0

                font=pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 40)
                text=font.render("GAME OVER", True, (255,0,0))
                screen.blit(text, (270, round(size[1]/2-50)))

                font = pygame.font.Font("C:/Windows/Fonts/ariblk.ttf", 40)
                score_text = font.render("score: {}".format(score), True, (0, 0, 255))
                screen.blit(score_text, (290, round(size[1] / 2 - 90)))

                pygame.display.flip()
            pygame.quit()

            usersscore[uid]=score
            userlist=sorted(usersscore.items(), key=operator.itemgetter(1),reverse=True)

            a.set(userlist[0][0])
            b.set(userlist[0][1])
            c.set(userlist[1][0])
            d.set(userlist[1][1])
            e.set(userlist[2][0])
            f.set(userlist[2][1])


        else:
            sentence.set('암호를 확인하세요.')

    else:
        if(uid==''):
            sentence.set('빈칸입니다. 아이디를 입력하세요.')
        else:
            sentence.set('등록된 아이디가 아닙니다.')




usersdata=dict()
usersscore=dict()
userlist=list()

loginPage=Tk()
loginPage.geometry('400x400+520+250')
loginPage.title("로그인")
loginPage.config(bg='beige')

firstLabel=Label(loginPage)
firstLabel.pack()
secondLabel=Label(loginPage)
secondLabel.pack()

lb1=Label(firstLabel, text='ID')
lb2=Label(secondLabel, text='PW')
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=0)


et1=Entry(firstLabel)
et2=Entry(secondLabel)
et1.grid(row=0, column=1)
et2.grid(row=0, column=1)

lb=Label(loginPage)
lb.pack()
bt1=Button(lb, text='회원가입', command=openjoinpage)
bt2=Button(lb, text='로그인', command=checkid)
bt1.grid(row=0, column=0, padx=10)
bt2.grid(row=0, column=1, padx=10)

sentence=StringVar(value=' ')
loginResult=Label(loginPage, width=24, textvariable=sentence, bg='beige')
loginResult.pack()

rankingResult=Label(loginPage, width=24, text="Ranking")
rankingResult.pack()

row1=Label(loginPage, width=24)
row1.pack()

row2=Label(loginPage, width=24)
row2.pack()

row3=Label(loginPage, width=24)
row3.pack()

row4=Label(loginPage, width=24)
row4.pack()

a=StringVar(value=' ')
b=StringVar(value=' ')
c=StringVar(value=' ')
d=StringVar(value=' ')
e=StringVar(value=' ')
f=StringVar(value=' ')

rankingLabel=Label(row1, width=8, text="순위")
rankingLabel.grid(row=0, column=0)

userLabel=Label(row1, width=8, text="아이디")
userLabel.grid(row=0, column=1)

scoreLabel=Label(row1,  width=8, text="점수")
scoreLabel.grid(row=0, column=2)

goldrankLabel = Label(row2, width=8, text=1)
goldrankLabel.grid(row=0, column=0)

goldidLabel=Label(row2, width=8, textvariable=a)
goldidLabel.grid(row=0, column=1)

goldscoreLabel=Label(row2,  width=8, textvariable=b)
goldscoreLabel.grid(row=0, column=2)


silverrankLabel = Label(row3, width=8, text=2)
silverrankLabel.grid(row=0, column=0)

silveridLabel=Label(row3, width=8, textvariable=c)
silveridLabel.grid(row=0, column=1)

silverscoreLabel=Label(row3,  width=8, text=userlist[1][1])
silverscoreLabel.grid(row=0, column=2)

brownrankLabel = Label(row4, width=8, text=3)
brownrankLabel.grid(row=0, column=0)

brownidLabel=Label(row4, width=8, text=userlist[2][0])
brownidLabel.grid(row=0, column=1)

brownscoreLabel=Label(row4,  width=8, text=userlist[2][1])
brownscoreLabel.grid(row=0, column=2)

loginPage.mainloop()