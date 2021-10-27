from tkinter import *

calculation = ""

def add_to_calculation(num):
    global calculation
    calculation += str(num)
    equation.set(calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        equation.set(calculation)
        calculation=""

    except:
        equation.set("error")
        calculation=""

def clear_field():
    global calculation
    calculation = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry("290x230")
    equation = StringVar()

text_results = Entry(root, textvariable= equation )
text_results.grid(columnspan=5, ipadx=80)

btn_1 = Button(root, text = "1", command=lambda:add_to_calculation(1), width=5,font= ("Arial",14))
btn_1.grid(row=2,column=0)

btn_2 = Button(root, text = "2", command=lambda:add_to_calculation(2), width=5,font= ("Arial",14))
btn_2.grid(row=2,column=1)

btn_3 = Button(root, text = "3", command=lambda:add_to_calculation(3), width=5,font= ("Arial",14))
btn_3.grid(row=2,column=2)

btn_4 = Button(root, text = "4", command=lambda:add_to_calculation(4), width=5,font= ("Arial",14))
btn_4.grid(row=3,column=0)

btn_5 = Button(root, text = "5", command=lambda:add_to_calculation(5), width=5,font= ("Arial",14))
btn_5.grid(row=3,column=1)

btn_6 = Button(root, text = "6", command=lambda:add_to_calculation(6), width=5,font= ("Arial",14))
btn_6.grid(row=3,column=2)

btn_7 = Button(root, text = "7", command=lambda:add_to_calculation(7), width=5,font= ("Arial",14))
btn_7.grid(row=4,column=0)

btn_8 = Button(root, text = "8", command=lambda:add_to_calculation(8), width=5,font= ("Arial",14))
btn_8.grid(row=4,column=1)

btn_9 = Button(root, text = "9", command=lambda:add_to_calculation(9), width=5,font= ("Arial",14))
btn_9.grid(row=4,column=2)

btn_0 = Button(root, text = "0", command=lambda:add_to_calculation(0), width=5,font= ("Arial",14))
btn_0.grid(row=5,column=1)

btn_plus = Button(root, text = "+", command=lambda:add_to_calculation("+"), width=7,font= ("Arial",14))
btn_plus.grid(row=2,column=3)

btn_minus = Button(root, text = "-", command=lambda:add_to_calculation("-"), width=7,font= ("Arial",14))
btn_minus.grid(row=3,column=3)

btn_multiply = Button(root, text = "*", command=lambda:add_to_calculation("*"), width=7,font= ("Arial",14))
btn_multiply.grid(row=4,column=3)

btn_divide = Button(root, text = "/", command=lambda:add_to_calculation("/"), width=7,font= ("Arial",14))
btn_divide.grid(row=5,column=3)

btn_open = Button(root, text = "(", command=lambda:add_to_calculation("("), width=5,font= ("Arial",14))
btn_open.grid(row=5,column=0)

btn_close = Button(root, text = ")", command=lambda:add_to_calculation(")"), width=5,font= ("Arial",14))
btn_close.grid(row=5,column=2)

btn_dec = Button(root, text = ".", command=lambda:add_to_calculation("."), width=7,font= ("Arial",14))
btn_dec.grid(row=6,column=3)

btn_equal = Button(root, text = "=", command=evaluate_calculation, width=5,font= ("Arial",14))
btn_equal.grid(row=6,column=2)

btn_clear = Button(root, text = "Clear", command=clear_field, width=11,font= ("Arial",14))
btn_clear.grid(row=6,column=0, columnspan = 2)
root.mainloop()
