import tkinter
import time
from tkinter import messagebox
from PIL import Image, ImageTk

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=1526, height=999, bg="white")

# 使用 Pillow 加載圖片
background_img = Image.open("picture.png")
wolf_img = Image.open("wolf.png")
sheep_img = Image.open("sheep.png")
cabbage_img = Image.open("cabbage.png")
boat_img = Image.open("boat.png")

background = ImageTk.PhotoImage(background_img)
wolf = ImageTk.PhotoImage(wolf_img)
sheep = ImageTk.PhotoImage(sheep_img)
cabbage = ImageTk.PhotoImage(cabbage_img)
boat = ImageTk.PhotoImage(boat_img)

global w_pos
global s_pos
global c_pos
global b_pos
w_pos = 0
s_pos = 0
c_pos = 0
b_pos = 0

def reset():
    canvas.delete("all")
    canvas.create_image(0, 0, anchor='nw', image=background)
    canvas.create_image(300,330, anchor='nw', image=wolf, tag="wolf")
    canvas.create_image(150, 300, anchor='nw', image=sheep, tag="sheep")
    canvas.create_image(0, 325, anchor='nw', image=cabbage, tag="cabbage")
    canvas.create_image(375, 225, anchor='nw', image=boat, tag="boat")
    global w_pos, s_pos, c_pos, b_pos
    w_pos, s_pos, c_pos, b_pos = 0, 0, 0, 0

reset()

#往右
def wgoright():
    global boat
    global sheep
    global wolf
    global cabbage
    global w_pos
    w_pos = 1
    global b_pos
    b_pos = 1
    canvas.delete("wolf")
    #canvas.create_image(1100,330,anchor='nw',image=wolf,tag="wolf")
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(375+5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("wolf")
        canvas.create_image(506+5*i,330,anchor='nw',image=wolf,tag="wolf") #806
        time.sleep(0.01)
        canvas.update()
    canvas.delete("wolf")
    canvas.create_image(1100,330,anchor='nw',image=wolf,tag="wolf")
        
def sgoright():
    global boat
    global sheep
    global wolf
    global cabbage
    global s_pos
    s_pos = 1
    global b_pos
    b_pos = 1
    canvas.delete("sheep")
    #canvas.create_image(1250,300,anchor='nw',image=sheep,tag="sheep")
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(375+5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("sheep")
        canvas.create_image(506+5*i,300,anchor='nw',image=sheep,tag="sheep")
        time.sleep(0.01)
        canvas.update()
    canvas.delete("sheep")
    canvas.create_image(1250,300,anchor='nw',image=sheep,tag="sheep")

def cgoright():
    global boat
    global sheep
    global wolf
    global cabbage
    global c_pos
    c_pos = 1
    global b_pos
    b_pos = 1
    b_pos = 1
    canvas.delete("cabbage")
    #canvas.create_image(1370,325,anchor='nw',image=cabbage,tag="cabbage")
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(375+5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("cabbage")
        canvas.create_image(506+5*i,330,anchor='nw',image=cabbage,tag="cabbage")
        time.sleep(0.01)
        canvas.update()
    canvas.delete("cabbage")
    canvas.create_image(1370,330,anchor='nw',image=cabbage,tag="cabbage")

def wgoleft():
    global boat
    global sheep
    global wolf
    global cabbage
    global w_pos
    w_pos = 0
    global b_pos
    b_pos = 0
    canvas.delete("wolf")
    canvas.create_image(300,330, anchor='nw', image=wolf,tag="wolf")
    
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(675-5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("wolf")
        canvas.create_image(806-5*i,330,anchor='nw',image=wolf,tag="wolf")
        time.sleep(0.01)
        canvas.update()
    canvas.delete("wolf")
    canvas.create_image(300,330,anchor='nw',image=wolf,tag="wolf")
    
    
def sgoleft():
    global boat
    global sheep
    global wolf
    global cabbage
    global s_pos
    s_pos = 0
    global b_pos

    b_pos = 0
    canvas.delete("sheep")
    canvas.create_image(150, 300, anchor='nw', image=sheep,tag="sheep")
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(675-5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("sheep")
        canvas.create_image(806-5*i,300,anchor='nw',image=sheep,tag="sheep")
        time.sleep(0.01)
        canvas.update()
    canvas.delete("sheep")
    canvas.create_image(150,300,anchor='nw',image=sheep,tag="sheep")

def cgoleft():
    global boat
    global sheep
    global wolf
    global cabbage
    global c_pos
    c_pos = 0
    global b_pos

    b_pos = 0
    canvas.delete("cabbage")
    canvas.create_image(0, 325, anchor='nw', image=cabbage,tag="cabbage")
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(675-5*i,225,anchor='nw',image=boat,tag="boat")
        canvas.delete("cabbage")
        canvas.create_image(806-5*i,330,anchor='nw',image=cabbage,tag="cabbage")
        time.sleep(0.01)
        canvas.update()
    canvas.delete("cabbage")
    canvas.create_image(0,325,anchor='nw',image=cabbage,tag="cabbage")

#def bgoleft():
 #   canvas.delete("boat")
  #  canvas.create_image(675-5*i,225,anchor='nw',image=boat,tag="boat")


    

def winornot():
    if((w_pos==s_pos)and(w_pos!=c_pos)and(w_pos!=b_pos)):
        #messagebox.showerror(message="羊被狼吃了")
        messagebox.showinfo(title="狼羊菜",message="羊被狼吃了OAO")
        reset()
    elif((s_pos==c_pos)and(s_pos!=w_pos)and(s_pos!=b_pos)):
        #messagebox.showerror(message="菜被羊吃了")
        messagebox.showinfo(title="狼羊菜",message="菜被羊吃了")
        reset()
    elif((w_pos==1) and (s_pos==1) and (c_pos==1)):
        #messagebox.showerror(message="恭喜過關")
        messagebox.showinfo(title="狼羊菜",message="恭喜過關")
        reset()

#按鈕介面:3
def btn1_move(): #狼走法
    global boat
    global w_pos
    global b_pos
    if(w_pos==0):
        #if(b_pos==1):
        #    boat_back()
        wgoright()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()
    elif(w_pos==1):
        #if(b_pos==0):
        #    boat_back()
        wgoleft()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()

def btn2_move(): #羊走法
    global s_pos
    global boat
    global b_pos
    if(s_pos==0):
        #if(b_pos==1):
        #    boat_back()
        sgoright()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()
    elif(s_pos==1):
        #if(b_pos==0):
        #    boat_back()
        sgoleft()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()
        

def btn3_move(): #菜走法
    global c_pos
    global boat
    global b_pos
    if(c_pos==0):
        #if(b_pos==1):
        #    boat_back()
        cgoright()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()
        #print(c_pos)
    elif(c_pos==1):
        #if(b_pos==0):
        #    boat_back()
        cgoleft()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
        winornot()
        #print(c_pos)

def bgoright():
    global b_pos
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(375+5*i,225,anchor='nw',image=boat,tag="boat")
        time.sleep(0.01)
        canvas.update()
    b_pos=1

def bgoleft():
    global b_pos
    for i in range(60):
        canvas.delete("boat")
        canvas.create_image(675-5*i,225,anchor='nw',image=boat,tag="boat")
        time.sleep(0.01)
        canvas.update()
    b_pos=0


def btn4_move():
    global b_pos
    if(b_pos==0):
        bgoright()
        winornot()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
    elif(b_pos==1):
        bgoleft()
        winornot()
        print(f'wolf_position:{w_pos}')
        print(f'sheep_position:{s_pos}')
        print(f'cabbage_position:{c_pos}')
        print(f'boat_position:{b_pos}')
        print()
          

btn1 = tkinter.Button(root,text="狼",font=15,command=btn1_move)
btn2 = tkinter.Button(root,text="羊",font=15,command=btn2_move)
btn3 = tkinter.Button(root,text="菜",font=15,command=btn3_move)
btn4 = tkinter.Button(root,text="船",font=15,command=btn4_move)
btn1.pack(anchor='n')
btn2.pack(anchor='n')
btn3.pack(anchor='n')
btn4.pack(anchor='n')

canvas.pack(side="bottom")
root.mainloop()