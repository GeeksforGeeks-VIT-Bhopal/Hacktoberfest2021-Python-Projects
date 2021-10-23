from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
window1 = Tk()
window1.title("To-Do List")
window1.geometry('400x400')
lb2 = Label(window1, text = 'Tasks:')
lb2.pack(pady = 10)
litbox1 = Listbox(window1, height = 10, width = 30, activestyle = 'dotbox')
litbox1.pack(pady = 10)
tasks = []
counter = 1
def clicked1():
    global counter
    window2 = Toplevel(window1)
    window2.title('Enter task information')
    window2.geometry('300x300')
    lb1 = Label(window2, text = 'Enter task name')
    lb1.pack(pady=10)
    ent1 = Entry(window2, width = 20)
    ent1.pack(pady = 10)
    def clicked4():
        global counter
        if ent1.get() == '':
            messagebox.showerror('Error', message = 'No Input')
            return
        task = ent1.get() + '\n'
        tasks.append(task)
        litbox1.insert(END, '(' + str(counter) + ')' + task)
        counter = counter + 1
        window2.destroy()
    btn3 = Button(window2, text = 'Save', command = clicked4)
    btn3.pack(pady = '10')
    def clicked7():
        window2.destroy()
    def clicked2():
        ent1.delete(0, 'end')
    btn4 = Button(window2, text = 'Clear', command = clicked2)
    btn4.pack(pady = 10)
    btn7 = Button(window2, text='Cancel', command=clicked7)
    btn7.pack(pady='10')
def clicked3():
    exit()
btn1 = Button(window1, text = 'Add a task',command = clicked1)
btn1.pack(pady = 10)
def clicked5():
    window3 = Toplevel(window1)
    window3.geometry('300x300')
    window3.title("Delete Task")
    lb2 = Label(window3, text = 'Enter the task no. to delete')
    lb2.pack(pady = 10)
    ent2 = Entry(window3, width = 5)
    ent2.pack(pady = 10)
    def clicked6():
        global counter
        if ent2.get() != int:
            messagebox.showerror('Error', message='Wrong Input! Please enter a valid number')
            return
        if ent2.get() == '':
            messagebox.showerror('Error', message = 'Please enter an integer')
        tno = int(ent2.get())
        if tno == 0:
            messagebox.showerror('Error', message='Wrong Input! Please enter a valid number')
        if tno>litbox1.size():
            messagebox.showerror('Error', message='Input value outside the range of number of tasks')
        litbox1.delete(tno - 1)
        counter = counter - 1
        window3.destroy()
    btn4 = Button(window3, text = 'Delete', command = clicked6)
    btn4.pack(pady = 10)
    def clicked2():
        ent2.delete(0, 'end')
    btn4 = Button(window3, text='Clear', command=clicked2)
    btn4.pack(pady=10)
    def clicked7():
        window3.destroy()
    btn7 = Button(window3, text='Cancel', command=clicked7)
    btn7.pack(pady='10')
btn2 = Button(window1, text = 'Delete a Task', command = clicked5)
btn2.pack(pady = 10)
def clicked2():
    global counter
    litbox1.delete(0, 'end')
    counter = 1
btn4 = Button(window1, text='Clear', command=clicked2)
btn4.pack(pady=10)
btn3 = Button(window1, text = 'Exit', command = clicked3)
btn3.pack(pady = 10)
mainloop()