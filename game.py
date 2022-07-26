# from cgitb import reset
from tkinter import*
import tkinter
from tkinter.font import BOLD
from turtle import clear, width

from PIL import ImageTk, Image

# from tkinter import ttk
# from tkinter import _Relief

import click

aarti_root = Tk()

import tkinter.messagebox
 
click= True
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()


image1 = Image.open("honey.jpeg")
resize_image1 = image1.resize((100, 160))
img1 = ImageTk.PhotoImage(resize_image1)
label1 = Label(image=img1)
label1.image = img1


image = Image.open("aarti.jpeg")
 
# Resize the image using resize() method
resize_image2 = image.resize((100, 160))
 
img = ImageTk.PhotoImage(resize_image2)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
# label1.pack()
 


def play():
    b1 = Button(aarti_root,width=10,height=9,text=" ", textvariable= btn1, bd=5,bg="grey",command=lambda: press(1,0,0))
    b2 = Button(aarti_root,width=10,height=9,text=" ", textvariable= btn2, bd=5,bg="grey",command=lambda: press(2,0,1))
    b3 = Button(aarti_root,width=10,height=9,text=" ",textvariable= btn3, bd=5,bg="grey",command=lambda: press(3,0,2))
    b4 = Button(aarti_root,width=10,height=9,text=" ",textvariable= btn4, bd=5,bg="pink",command=lambda: press(4,1,0))
    b5 = Button(aarti_root,width=10,height=9,text=" " ,textvariable= btn5, bd=5,bg="pink",command=lambda: press(5,1,1))
    b6 = Button(aarti_root,width=10,height=9,text=" " ,textvariable= btn6, bd=5,bg="pink",command=lambda: press(6,1,2))
    b7 = Button(aarti_root,width=10,height=9,text=" " ,textvariable= btn7, bd=5,bg="yellow",command=lambda: press(7,2,0))
    b8 = Button(aarti_root,width=10,height=9,text=" " ,textvariable= btn8, bd=5,bg="yellow",command=lambda: press(8,2,1))
    b9 = Button(aarti_root,width=10,height=9,text=" ", textvariable= btn9, bd=5,bg="yellow",command=lambda: press(9,2,2))
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

    def press(num,r,c):
      global click,count
      if click == True:
        label1 = Label(aarti_root,image=img1)
        label1 = Label(image=img1)
        label1.image = img1
        label1.grid(row=r,column=c)

 
    
        if num==1:
            btn1.set("X")
        if num==2:
            btn2.set("X")
        if num==3:
            btn3.set("X")
        if num==4:
            btn4.set("X")
        if num==5:
            btn5.set("X")
        if num==6:
            btn6.set("X")
        if num==7:
            btn7.set("X")
        if num==8:
            btn8.set("X")
        else:
            btn9.set("X")
        count+=1
        click=False
      else:
        label = Label(aarti_root,image=img)
        label = Label(image=img)
        label.image = img
        label.grid(row=r,column=c)


        if num==1:
            btn1.set("O")
        if num==2:
            btn2.set("O")
        if num==3:
            btn3.set("O")
        if num==4:
            btn4.set("O")
        if num==5:
            btn5.set("O")
        if num==6:
            btn6.set("O")
        if num==7:
            btn7.set("O")
        if num==8:
            btn8.set("O")
        else:
            btn9.set("O")
    
        count+=1
        click=True
        check_win()
    
    def check_win():
        global count , click
        if (btn1.get()=="X" and btn2.get()=="X" and btn3.get()=="X" or btn4.get()=="X" and btn5.get()=="X" and btn6.get()=="X" or  btn7.get()=="X" and btn8.get()=="X" and btn9.get()=="X" or btn1.get()=="X" and btn4.get()=="X" and btn7.get()=="X" or btn2.get()=="X" and btn5.get()=="X" and btn8.get()=="X" or btn3.get()=="X" and btn6.get()=="X" and btn9.get()=="X" or btn1.get()=="X" and btn5.get()=="X" and btn9.get()=="X" or btn3.get()=="X" and btn5.get()=="X" and btn7.get()=="X"):




            # btn4.get()=="X" and btn5.get()=="X" and btn6.get()=="X" or 
            # btn7.get()=="X" and btn8.get()=="X" and btn9.get()=="X" or
            # btn1.get()=="X" and btn4.get()=="X" and btn7.get()=="X" or
            # btn2.get()=="X" and btn5.get()=="X" and btn8.get()=="X" or
            # btn3.get()=="X" and btn6.get()=="X" and btn9.get()=="X" or
            # btn1.get()=="X" and btn5.get()=="X" and btn9.get()=="X" or
            # btn3.get()=="X" and btn5.get()=="X" and btn7.get()=="X"):
            tkinter.messagebox.showinfo("tic tac toe","Honey won the match")
            click = True
            count = 0
            clear()
            play()
            
      
        if (btn1.get()=="O" and btn2.get()=="O" and btn3.get()=="O" or btn4.get()=="O" and btn5.get()=="O" and btn6.get()=="O" or  btn7.get()=="O" and btn8.get()=="O" and btn9.get()=="O" or btn1.get()=="O" and btn4.get()=="O" and btn7.get()=="O" or btn2.get()=="O" and btn5.get()=="O" and btn8.get()=="O" or btn3.get()=="O" and btn6.get()=="O" and btn9.get()=="O" or btn1.get()=="O" and btn5.get()=="O" and btn9.get()=="O" or btn3.get()=="O" and btn5.get()=="O" and btn7.get()=="O"):
      


        # elif (btn1.get()=="O" and btn2.get()=="O" and btn3.get()=="O" or 
        #       btn4.get()=="O" and btn5.get()=="O" and btn6.get()=="O" or 
        #       btn7.get()=="O" and btn8.get()=="O" and btn9.get()=="O" or
        #       btn1.get()=="O" and btn4.get()=="O" and btn7.get()=="O" or
        #       btn2.get()=="X" and btn5.get()=="X" and btn8.get()=="X" or
        #       btn3.get()=="O" and btn6.get()=="O" and btn9.get()=="O" or
        #       btn1.get()=="O" and btn5.get()=="O" and btn9.get()=="O" or
        #       btn3.get()=="O" and btn5.get()=="O" and btn7.get()=="O"):
              tkinter.messagebox.showinfo("tic tac toe","Aarti won the match")
              click = False
              count = 0
              clear()
              play()
              dis()
        elif count == 9:
                tkinter.messagebox.showinfo("tic tac toe","Game tie")
                click = False
                count = 0 
                clear()

            
    def clear():
        btn1.set("")
        btn2.set("")
        btn3.set("")
        btn4.set("")
        btn5.set("")
        btn6.set("")
        btn7.set("")
        btn8.set("")
        btn9.set("")
    def dis():
        pass
play()
aarti_root.mainloop()