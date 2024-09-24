import tkinter
from tkinter import messagebox
import time

root = tkinter.Tk()
root.title("老鼠走迷宮")
canvas = tkinter.Canvas(width=800,height=800,bg="white")
img = tkinter.PhotoImage(file="mimi_s.png")
c_x = 0
c_y = 0
move = 1
x = 0
y = 2
step=0 #走第幾步 
stepx=[0]*1000
stepy=[0]*1000
maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #y/cx軸
        [2, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #x/cy軸
    ]

def ini_proc():
    i=0
    j=0
    #迷宮圖形 10*10
    #1代表牆壁，0代表通道，2代表起點，3代表終點,如果為4:則代表該支線路段不通
    global maze
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #y軸
        [2, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #x軸
    ]
    for i in range(10):
        for j in range(10):
            if(maze[i][j]==0 or maze[i][j]==2 or maze[i][j]==3):
                canvas.create_rectangle(j*80,i*80,j*80+79,i*80+79,fill="white")
            elif(maze[i][j]==1):
                canvas.create_rectangle(j*80,i*80,j*80+79,i*80+79,fill="skyblue")
    #charater position
    global c_x,c_y,move,x,y,step,stepx,stepy
    c_x = 0
    c_y = 0
    move = 1
    x = 0
    y = 2
    step=0 #走第幾步 
    stepx=[0]*1000
    stepy=[0]*1000
    canvas.create_image(40,120,image=img,tag="Cat")

ini_proc()
#主程式
def main_proc():
    global x,y,c_x,c_y,move
    c_x = stepy[move]
    c_y = stepx[move]
    canvas.coords("Cat",c_x*80+40,c_y*80+40)
    move = move+1
    if(maze[c_x][c_y]==3 or maze[c_x][c_y]==2):
        canvas.create_rectangle(c_y*80,c_x*80,c_y*80+79,c_x*80+79,fill="yellow")
    if(maze[c_x][c_y]==4):
        canvas.create_rectangle(c_y*80,c_x*80,c_y*80+79,c_x*80+79,fill="red")
    canvas.delete("Cat")
    canvas.create_image(c_y*80+40,c_x*80+40,image=img,tag="Cat")
    print(f"c_x: {c_x}")
    print(f"c_y: {c_y}")
    print(f"maze[{c_x}][{c_y}]: {maze[c_x][c_y]}")
    print()
    if (maze[c_x][c_y]==3):
        messagebox.showinfo(title="老鼠走迷宮",message="成功了!!!")
        ini_proc()
        bg_func()
        main_proc()
    else:
        root.after(100,main_proc)
    
        
        
#當主程式執行時立即執行    

def bg_func():
    global x,y,step,stepx,stepy,maze
    while(1):
        if (maze[y-1][x]==3 or maze[y+1][x]==3 or maze[y][x-1]==3 or maze[y][x+1]==3):
            if (maze[y-1][x]==3):
                y=y-1
            elif (maze[y+1][x]==3):
                y=y+1
            elif (maze[y][x-1]==3):
                x=x-1
            elif (maze[y][x+1]==3):
                x=x+1
            step=step+1
            stepx[step]=x
            stepy[step]=y
            break
        elif (maze[y-1][x]==0 or maze[y+1][x]==0 or maze[y][x-1]==0 or maze[y][x+1]==0):
            if (maze[y-1][x]==0):
                y=y-1
            elif (maze[y][x+1]==0):
                x=x+1
            elif (maze[y+1][x]==0):
                y=y+1
            elif (maze[y][x-1]==0):
                x=x-1
            step=step+1
            maze[y][x]=2
            stepx[step]=x
            stepy[step]=y
        else:
            maze[y][x]=4
            if (maze[y-1][x]==2):
                y=y-1
            elif (maze[y][x+1]==2):
                x=x+1
            elif (maze[y+1][x]==2):
                y=y+1
            elif (maze[y][x-1]==2):
                x=x-1
            step=step+1
            stepx[step]=x
            stepy[step]=y
bg_func()
main_proc()
for y in range(10):
    print(maze[y])
canvas.pack()
root.mainloop()