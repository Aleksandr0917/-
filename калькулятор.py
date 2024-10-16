import tkinter as tk
from idlelib.colorizer import color_config

from modul_3_3 import values_list_2


def get_num():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def answer_values(values):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)
    return values


def add():
    num1, num2 = get_num()       # num1 = int(number1_entry.get())
                                 # num2 = int(number2_entry.get())
    res = num1 + num2
    answer_values(res)           # answer_entry.delete(0, 'end')
                                 # answer_entry.insert(0, res)


def sub():
    num1, num2 = get_num()              #num1 = int(number1_entry.get())
                                        #num2 = int(number2_entry.get())
    res = num1 - num2
    answer_values(res)                  # answer_entry.delete(0, 'end')
                                       #  answer_entry.insert(0, res)


def mul():
    num1, num2 = get_num()
    res = num1 * num2
    answer_values(res)


def div():
    num1, num2 = get_num()
    res = num1 / num2
    answer_values(res)


windows = tk.Tk()
windows.title('Калькулятор')
windows.config(bg='gold')
windows.geometry("400x400")
windows.resizable(False, False)
button_add = tk.Button(windows, text='+', width=2, height=2, command=add)
button_add.config(bg='red')
button_add.place(x=100, y=240)
button_sub = tk.Button(windows,  text='-', width=2, height=2, command=sub)
button_sub.config(bg='yellow')
button_sub.place(x=150, y=240)
button_mul = tk.Button(windows, text='*', width=2, height=2, command=mul)
button_mul.config(bg='green')
button_mul.place(x=200, y=240)
button_div = tk.Button(windows, text='/', width=2, height=2, command=div)
button_div.config(bg='blue')
button_div.place(x=250, y=240)
number1_entry = tk.Entry(windows, width=25)
number1_entry.config(bg='gray')
number1_entry.place(x=100, y=60)
number2_entry = tk.Entry(windows, width=25)
number2_entry.config(bg='gray')
number2_entry.place(x=100, y=160)
answer_entry = tk.Entry(windows, width=25)
answer_entry.config(bg='gray')
answer_entry.place(x=100, y=330)
number1 = tk.Label(windows, text='Введите первое значение:', bg='violet')
number1.place(x=100, y=30)
number2 = tk.Label(windows, text='Введите второе значение:', bg='light blue')
number2.place(x=100, y=130)
answer = tk.Label(windows, text='Ответ:')
answer.place(x=100, y=300)
windows.mainloop()
#  pip install auto-py-to-exe