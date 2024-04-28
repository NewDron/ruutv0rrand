from tkinter import *
import math

def get_text():
    is_valid=True
    for entry in [ax,bx,cx]:
        if entry.get():
            entry.config(bg='pink')
        else:
            entry.config(bg='red')
            is_valid=False
        if is_valid:
            a=ax.get()
            b=bx.get()
            c=cx.get()
            d = (float(b) ** 2) - (4 * float(a) * float(c))
            if d == 0:
                x0 = -float(b) / (2 * float(a))
                vastus.config(text="D="+str(d)+", x= "+str(x0))
            elif d > 0:
                x1 = (-float(b) + math.sqrt(float(d))) / (2 * float(a))
                x2 = (-float(b) + math.sqrt(float(d))) / (2 * float(a))
                vastus.config(text="D="+str(d)+", x1= "+str(x1)+", x2= "+str(x2))
            elif d < 0:
                vastus.config(text="D="+str(d)+", Корней нет")
            else:
                vastus.config(text="error")

aken=Tk()
aken.geometry("400x200")
aken.title("Ruutvõrrandi lahendamine")
aken.iconbitmap("2.ico")
t=" Решение квадратного уравнения "
f1=Frame(aken,bg="blue",borderwidth=10,height=50,width=600)
l=Label(f1,text=t,bg="red",fg="yellow",font="consolas 16",height=3,width=len(t))
f2=Frame(aken,bg="green",border=5,height=200,width=200)
ax=Entry(f2,bg="pink",fg="brown",font="impact 20",width=4)
x1text=Label(f2,text="x**2+",bg="green",font="impact 20")
bx=Entry(f2,bg="pink",fg="brown",font="impact 20",width=4)
x2text=Label(f2,text="x+",bg="green",font="impact 20")
cx=Entry(f2,bg="pink",fg="brown",font="impact 20",width=4) 
x3text=Label(f2,text="=0",bg="green",font="impact 20")
bu=Button(f2,text="Решить",bg="cyan",font="tahoma 14",relief=GROOVE, command=get_text)
f3=Frame(aken,bg="orange",border=5,height=100,width=200)
vastus=Label(f3)

l.pack()
f1.grid(row=0,column=0)
f2.grid(row=1,column=0)
obj=[ax,x1text,bx,x2text,cx,x3text,bu,vastus]
i=0
for o in obj:
    o.grid(row=1, column=i)
    i+=1
f2.grid(row=2,column=0,columnspan=6)
f3.grid(row=3, column=0)

aken.mainloop()
