from tkinter import* 
me=Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me,text="CALCULATE HERE",bg='PINK',font=("ARIAL",25))
melabel.pack(side=TOP)
me.config(background='BROWN')

displayStr=StringVar()
op=""

def but(a):
    global op
    op=op+str(a)
    displayStr.set(op)
    
    
def eq():
    global op
    result=str(eval(op))
    displayStr.set(result)
    op=""
     
def clrbut():
     displayStr.set('')
     
     
inputText=Entry(me,font=("Courier New",12,'bold'),textvar=displayStr,width=25,bd=5,bg='WHITE')
inputText.pack()

but1=Button(me,padx=14,pady=14,bd=4,bg='RED',command=lambda:but(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(me,padx=14,pady=14,bd=4,bg='RED',command=lambda:but(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(me,padx=14,pady=14,bd=4,bg='RED',command=lambda:but(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(me,padx=14,pady=14,bd=4,bg='YELLOW',command=lambda:but(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(me,padx=14,pady=14,bd=4,bg='RED',command=lambda:but(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(me,padx=47,pady=14,bd=4,bg='YELLOW',command=lambda:but("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(me,padx=14,pady=14,bd=4,bg='ORANGE',text="+",command=lambda:but("+"),font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(me,padx=14,pady=14,bd=4,bg='ORANGE',text="-",command=lambda:but("-"),font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(me,padx=14,pady=14,bd=4,bg='ORANGE',text="*",command=lambda:but("*"),font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(me,padx=14,pady=14,bd=4,bg='ORANGE',text="/",command=lambda:but("/"),font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(me,padx=14,pady=119,bd=4,bg='GREEN',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(me,padx=151,pady=14,bd=4,bg='GREEN',command=eq,text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
me.mainloop()