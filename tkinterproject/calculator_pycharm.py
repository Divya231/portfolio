from tkinter import *

root=Tk()
root.config(bg="lemon chiffon")
def click(event):
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root.geometry("585x689")
root.title("Calculator")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

#
# f=Frame(root,bg="thistle 1",borderwidth=10,relief=SUNKEN)
# f.pack(side=TOP,fill="x")
# Label(f,text="My Calculator")
f1=Frame(root,bg="peach puff")
b1=Button(f1,text="9",padx=15,pady=15,font="lucida 15 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="8",padx=15,pady=15,font="lucida 15 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)


b1=Button(f1,text="7",padx=15,pady=15,font="lucida 15 bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind("<Button-1>",click)
f1.pack()

f2=Frame(root,bg="grey")
b2=Button(f2,text="6",padx=15,pady=15,font="lucida 15 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)


b2=Button(f2,text="5",padx=15,pady=15,font="lucida 15 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)

b2=Button(f2,text="4",padx=15,pady=15,font="lucida 15 bold")
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind("<Button-1>",click)
f2.pack()

f3=Frame(root,bg="peach puff")
b3=Button(f3,text="3",padx=15,pady=15,font="lucida 15 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b3=Button(f3,text="2",padx=15,pady=15,font="lucida 15 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)

b3=Button(f3,text="1",padx=15,pady=15,font="lucida 15 bold")
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind("<Button-1>",click)
f3.pack()

f4=Frame(root,bg="grey")
b4=Button(f4,text="0",padx=15,pady=15,font="lucida 15 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)

b4=Button(f4,text="+",padx=15,pady=15,font="lucida 15 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)


b4=Button(f4,text="-",padx=15,pady=15,font="lucida 15 bold")
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind("<Button-1>",click)
f4.pack()

f5=Frame(root,bg="peach puff")
b5=Button(f5,text="*",padx=15,pady=15,font="lucida 15 bold")
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind("<Button-1>",click)

b5=Button(f5,text="/",padx=15,pady=15,font="lucida 15 bold")
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind("<Button-1>",click)


b5=Button(f5,text=".",padx=15,pady=15,font="lucida 15 bold")
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind("<Button-1>",click)

b5=Button(f5,text="C",padx=15,pady=15,font="lucida 15 bold")
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind("<Button-1>",click)
f5.pack()


f6=Frame(root,bg="grey")
b6=Button(f6,text="(",padx=15,pady=15,font="lucida 15 bold")
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind("<Button-1>",click)

b6=Button(f6,text=")",padx=15,pady=15,font="lucida 15 bold")
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind("<Button-1>",click)

b6=Button(f6,text="%",padx=15,pady=15,font="lucida 15 bold")
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind("<Button-1>",click)


b6=Button(f6,text="=",padx=15,pady=15,font="lucida 15 bold")
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind("<Button-1>",click)
f6.pack()
root.mainloop()