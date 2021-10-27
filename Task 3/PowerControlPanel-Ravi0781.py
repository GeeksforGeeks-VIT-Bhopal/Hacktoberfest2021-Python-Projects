import os
from tkinter import *
from tkinter.ttk import *
window1 = Tk()
window1.title("Power Options")
window1.geometry('300x300')
def clicked0():
    os.system('shutdown /s /t 1')
def clicked1():
    window2 = Toplevel(window1)
    window2.title("Confirmation Page")
    lb1 = Label(window2, text = "Are you sure you want to Shut Down?")
    lb1.pack(pady=10)
    btn2 = Button(window2, text = 'Yes', command = clicked0)
    btn2.pack(pady=20)
    def clicked00():
        window2.destroy()
    btn3 = Button(window2, text = 'No', command = clicked00)
    btn3.pack(pady=20)
    window2.geometry('300x300')
btn1 = Button(window1,text = 'Shut Down', command = clicked1)
btn1.pack(pady=10)
def clicked2():
    os.system('shutdown /r /t 1')
def clicked4():
    window2 = Toplevel(window1)
    window2.title("Confirmation Page")
    lb1 = Label(window2, text="Are you sure you want to Restart?")
    lb1.pack(pady=10)
    btn2 = Button(window2, text = 'Yes', command = clicked2)
    btn2.pack(pady=20)
    def clicked3():
        window2.destroy()
    btn3 = Button(window2, text = 'No', command = clicked3)
    btn3.pack(pady=20)
    window2.geometry('300x300')
btn2 = Button(window1,text = 'Restart', command = clicked4)
btn2.pack(pady=10)
def clicked5():
    os.system('shutdown.exe /h')
def clicked7():
    window2 = Toplevel(window1)
    window2.title("Confirmation Page")
    lb1 = Label(window2, text = "Are you sure you want to Hibernate?")
    lb1.pack(pady=10)
    btn2 = Button(window2, text = 'Yes', command = clicked5)
    btn2.pack(pady=20)
    def clicked6():
        window2.destroy()
    btn3 = Button(window2, text = 'No', command = clicked6)
    btn3.pack(pady=20)
    window2.geometry('300x300')
btn3 = Button(window1,text = 'Hibernate', command = clicked7)
btn3.pack(pady=10)
mainloop()