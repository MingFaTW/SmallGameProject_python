import tkinter
import random
import time
import sys
import os
from tkinter import *
root = tkinter.Tk()
#root.title("CBB110213 李明發 poker Homework")
Lab0 = Label(root,text="Poker比大小",font=15,width=1600,bg="Lightyellow")
Lab0.pack()
Lab1 = tkinter.Label(root, text="Player A", font=("Arial", 15),fg="black",bg="white")
Lab2 = tkinter.Label(root, text="Player B", font=("Arial", 15),fg="black",bg="white")
Lab1.pack()
Lab2.pack()

card4 = ["梅花 01.png","梅花 02.png","梅花 03.png","梅花 04.png","梅花 05.png","梅花 06.png","梅花 07.png","梅花 08.png","梅花 09.png","梅花 10.png","梅花 11.png","梅花 12.png","梅花 13.png"]
card1 = ["黑桃 01.png","黑桃 02.png","黑桃 03.png","黑桃 04.png","黑桃 05.png","黑桃 06.png","黑桃 07.png","黑桃 08.png","黑桃 09.png","黑桃 10.png","黑桃 11.png","黑桃 12.png","黑桃 13.png"]
card2 = ["方塊 01.png","方塊 02.png","方塊 03.png","方塊 04.png","方塊 05.png","方塊 06.png","方塊 07.png","方塊 08.png","方塊 09.png","方塊 10.png","方塊 11.png","方塊 12.png","方塊 13.png"]
card3 = ["紅心 01.png","紅心 02.png","紅心 03.png","紅心 04.png","紅心 05.png","紅心 06.png","紅心 07.png","紅心 08.png","紅心 09.png","紅心 10.png","紅心 11.png","紅心 12.png","紅心 13.png"]
card5 = card1+card2+card3+card4
canvas = tkinter.Canvas(root,width=1600,height=900)  

i=0
j=0

img=[None]*5
img1=[None]*5
cards1_color=[None]*5
cards1_num=[0,0,0,0,0]
cards2_color=[None]*5
cards2_num=[None]*5


def main():
    for i in range(5):
        x=random.choice(card5)
        cards1_color[i]=x[:2]
        cards1_num[i]=int(x[3:5]) #char to ascii
        
        print('PlayerA[{2}],{0},{1}'.format(cards1_color[i],cards1_num[i],i))
        
        img[i] = tkinter.PhotoImage(file=x)
        y=random.choice(card5)
        cards2_color[i]=y[:2]
        cards2_num[i]=int(y[3:5])
        
        print('PlayerB[{2}],{0},{1}'.format(cards2_color[i],cards2_num[i],i))
        
        img1[i] = tkinter.PhotoImage(file=y)
        
        canvas.create_image(100+i*200,500,anchor="sw",image=img1[i])
        canvas.create_image(100+i*200,10,anchor="nw",image=img[i])
        time.sleep(0.1)    
        canvas.update()

    count=[0,0,0,0,0]  #計算有多少pair
    Key_A=0    #playerA,預設為牌組類型，並參考下方dict設定
    Key_B=0    #playerB,預設為牌組類型，並參考下方dict設定
    colorsA=0    #playerA,看牌組顏色是否相同 : 3
    colorsB=0    #playerB,看牌組顏色是否相同 : 3        
    temp=0          #暫存值

    #####################

    n = len(cards1_num)
    for i in range(n-2):                   
        for j in range(n-i-1):            
            if cards1_num[j] > cards1_num[j+1]:        
                cards1_num[j], cards1_num[j+1] = cards1_num[j+1], cards1_num[j]
                cards1_color[j], cards1_color[j+1] = cards1_color[j+1], cards1_color[j]
    print(cards1_num)   
    print(cards1_color)

    ######################

    n = len(cards2_num)
    for i in range(n-2):                   # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字 
            if cards2_num[j] > cards2_num[j+1]:        # 比大小然後互換
                cards2_num[j], cards2_num[j+1] = cards2_num[j+1], cards2_num[j]
                cards2_color[j], cards2_color[j+1] = cards2_color[j+1], cards2_color[j]
    print(cards2_num)   
    print(cards2_color)


    ######################

    com={-1:"皇家同花順",0:"同花順",1:"四條",2:"葫蘆",3:"同花",4:"順子",5:"三條",6:"兩對",7:"一對",8:"高牌"}


    i=0
    j=0 
    #A牌組

   
    #辨識牌組OAO
    #A牌組
    #是不是同花色
    temp=0
    for i in range(5):
        if(cards1_color[0]==cards1_color[i]):
            temp=temp+1
        if temp == 5:
            colorsA=1
        else:
            colorsA=0
    print(f"colorsA={colorsA}")    
        
    result=0
    num=0#牌值相同的個數
    for A in range(0, 5):#統計相等的個數 或者是否為順子
        if cards1_num[A-1]- cards1_num[A]== 1:
            result += 1#如果為順子，則resul=4
        elif cards1_num[A] == cards1_num[A - 1]:
            num += 1

    if colorsA==1:#同花
        if cards1_num==[13,12,11,10,9]:#皇傢同花順
            Key_A = -1
        elif result==4:#同花順
            Key_A = 0
        else:
            Key_A=3#同花
    if colorsA==0:#非同花
        if num==3:#四條或葫蘆
            if cards1_num[1]==cards1_num[2]==cards1_num[3]==cards1_num[4] or cards1_num[0]==cards1_num[1]==cards1_num[2]==cards1_num[3]:
                Key_A=1#四條
            else:
                Key_A=2#葫蘆
        elif result==4:#順子
            Key_A=4
        elif num==2:#三條或兩隊
            if cards1_num[0]==cards1_num[1]==cards1_num[2] or cards1_num[1]==cards1_num[2]==cards1_num[3] or cards1_num[2]==cards1_num[3]==cards1_num[4]:
                Key_A=5#三條
            else:
                Key_A=6#兩隊
        elif num==1:#一對
            Key_A=7
        else:
            Key_A=8#高牌
            
            
    #B牌組
    #是不是同花色
    temp=0
    for i in range(5):
        if(cards2_color[0]==cards2_color[i]):
            temp=temp+1
        if temp == 5:
            colorsB=1
        else:
            colorsB=0
    print(f"colorsB={colorsB}")    
        
    result=0
    num=0#牌值相同的個數
    for B in range(0, 5):#統計相等的個數 或者是否為順子
        if cards2_num[B-1]- cards2_num[B]== 1:
            result += 1#如果為順子，則resul=4
        elif cards2_num[B] == cards2_num[B - 1]:
            num += 1

    if colorsB==1:#同花
        if cards2_num==[13,12,11,10,9]:#皇傢同花順
            Key_B = -1
        elif result==4:#同花順
            Key_B = 0
        else:
            Key_B=3#同花
    if colorsB==0:#非同花
        if num==3:#四條或葫蘆
            if cards2_num[1]==cards2_num[2]==cards2_num[3]==cards2_num[4] or cards2_num[0]==cards2_num[1]==cards2_num[2]==cards2_num[3]:
                Key_B=1#四條
            else:
                Key_B=2#葫蘆
        elif result==4:#順子
            Key_B=4
        elif num==2:#三條或兩隊
            if cards2_num[0]==cards2_num[1]==cards2_num[2] or cards2_num[1]==cards2_num[2]==cards2_num[3] or cards2_num[2]==cards2_num[3]==cards2_num[4]:
                Key_B=5#三條
            else:
                Key_B=6#兩隊
        elif num==1:#一對
            Key_B=7
        else:
            Key_B=8#高牌

    winner=-1 #A贏則0，B贏則1     
    if(Key_A<Key_B):
        winner=0
    elif(Key_A>Key_B):
        winner=1
    elif(Key_A==Key_B):
        if(Key_A==0): #同花順
            if(cards1_num[4]>cards2_num[4]):
                winner=0
            elif(cards1_num[4]==cards2_num[4]):
                winner=2
            else:
                winner=1
        if(Key_A==1): #四條
            if(cards1_num[0]>cards2_num[0]):
                winner=0
            elif(cards1_num[0]==cards2_num[0]):
                if(cards1_num[4]>cards2_num[4]): #前四張相同，對比最後一張
                    winner=0
                elif(cards1_num[4]==cards2_num[4]): #完全相同
                    winner=2
            else:
                winner=1
        if(Key_A==2): #葫蘆
            if(cards1_num[0]>cards2_num[0]):
                winner=0
            elif(cards1_num[0]==cards2_num[0]):
                if(cards1_num[3]>cards2_num[3]): #後兩張
                    winner=0
                elif(cards1_num[3]==cards2_num[3]):
                    winner=2
                else:
                    winner=1
            else:
                winner=1
        if(Key_A==3): #同花
            for i in range(5):
                if(cards1_num[i]>cards2_num[i]):
                    winner=0
                elif(cards1_num[i]<cards2_num[i]):
                    winner=1
                else:
                    winner=2
        if(Key_A==4): #順子
            for i in range(5):
                if(cards1_num[i]>cards2_num[i]):
                    winner=0
                elif(cards1_num[i]<cards2_num[i]):
                    winner=1
                else:
                    winner=2
        if(Key_A==5): #三條
            if(cards1_num[0]>cards2_num[0]):
                winner=0
            elif(cards1_num[0]<cards2_num[0]):
                winner=1
            else:
                for i in range(3,5):
                    if(cards1_num[i]>cards2_num[i]):
                        winner=0
                    elif(cards1_num[i]<cards2_num[i]):
                        winner=1
                    else:
                        winner=2
        if(Key_A==6): #兩對
            if(cards1_num[0]>cards2_num[0]):
                winner=0
            elif(cards1_num[0]<cards2_num[0]):
                winner=1
            else:
                if(cards1_num[2]>cards2_num[2]):
                    winner=0
                elif(cards1_num[2]<cards2_num[2]):
                    winner=1
                else:
                    if(cards1_num[4]>cards2_num[4]):
                        winner=0
                    elif(cards1_num[4]<cards2_num[4]):
                        winner=1
                    else:
                        winner=2
        if(Key_A==7):
            if(cards1_num[0]>cards2_num[0]):
                winner=0
            elif(cards1_num[0]<cards2_num[0]):
                winner=1
            else:
                for i in range(2,5):
                    if(cards1_num[i]>cards2_num[i]):
                        winner=0
                    elif(cards1_num[i]<cards2_num[i]):       
                        winner=1
                    elif(i==4):
                        if(cards1_num[4]==cards2_num[4]):
                            winner=2
        if(Key_A==8):
            for i in range(0,5):
                if(cards1_num[i]>cards2_num[i]):
                    winner=0
                elif(cards1_num[i]<cards2_num[i]):       
                    winner=1
                elif(i==4):
                    if(cards1_num[4]==cards2_num[4]):
                        winner=2
          
    
    Lab1 = tkinter.Label(root, text=f"Player A 是 {com[Key_A]}", font=("Arial", 15),fg="black",bg="white")
    Lab2 = tkinter.Label(root, text=f"Player B 是 {com[Key_B]}", font=("Arial", 15),fg="black",bg="white")
    Lab2.pack(side=BOTTOM)  
    Lab1.pack(side=BOTTOM) 

    if(winner==0):
        Lab3 = tkinter.Label(root,text=f"Player A is winner",font=("Arial", 15),width=1600,fg="black",bg="white")
        print("Player A is winner")
    elif(winner==1):
        Lab3 = tkinter.Label(root,text=f"Player B is winner",font=("Arial", 15),width=1600,fg="black",bg="white")
        print("Player B is winner")
    elif(winner==2):
        Lab3 = tkinter.Label(root,text=f"Two players draw",font=("Arial", 15),width=1600,fg="black",bg="white")
        print("Two Players draw")


    Lab3.pack(side=BOTTOM)  
    
    canvas.update()
    root.update()
    
    canvas.pack()
    root.mainloop()

####################################
'''
def replay():
    # 清除 canvas 的所有內容
    canvas.delete("all")
    
    global cards1_color, cards1_num, cards2_color, cards2_num, img, img1
    
    # 重置遊戲數據
    cards1_color = [None] * 5
    cards1_num = [0, 0, 0, 0, 0]
    cards2_color = [None] * 5
    cards2_num = [None] * 5
    img = [None] * 5
    img1 = [None] * 5
    
    # 清除所有 Label
    for widget in root.pack_slaves():
        if isinstance(widget, Label):
            widget.destroy()
        
    # 重置遊戲
    main()

btn2 = Button(root,text="Replay",width=15,font=15,command=replay)
btn2.pack(anchor=S,side=BOTTOM,padx=5,pady=5) 
'''
###################################

main()
