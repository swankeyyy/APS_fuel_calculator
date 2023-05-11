import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox
import main
window = tk.Tk()

window.title('Calc v 1.1')
window.geometry('800x400+200+100')

def clicked():
    messagebox.showinfo('Заголовок', 'KJHFJKSHDFKJHSKFkhfks')
# поле выбора страны и выпадающий список стран

country_label = tk.Label(text='Страна:', font='Arial 15').grid(row=0, column=0)
countries = ('Европа, Беларусь', 'СНГ')
country_box = ttk.Combobox(width=25,height=10, values=countries)
country_box.grid(row=1, column=0)

# поле и кнопка ввода расстояния

ent_dist_label = tk.Label(text='Расстояние, км:', font='Arial 15').grid(row=2, column=0, ipady=3)
ent_dist = tk.Entry(width=60)
ent_dist.grid(row=3, column=0, columnspan=1, padx=4, pady=5, ipadx=3, ipady=3)


# поле ввода веса

ent_weight_label = tk.Label(text='Вес груза с точностью до грамм:', font='Arial 15').grid(row=4, column=0, ipady=3)
ent_weight = tk.Entry(width=60)
ent_weight.grid(row=5, column=0, columnspan=1, padx=4, pady=5, ipadx=3, ipady=3)


def clicked():
    """Импорт функции из main и передача данных из полей ввода"""
    distance = ent_dist.get()
    weight = ent_weight.get()
    coefficient = country_box.get()
    result = main.calculating(distance, weight, coefficient)
    messagebox.showinfo('Топливо:', result)


# кнопка расчета топлива

ent_weight_button = tk.Button(text='Посчитать топливо', command=clicked).grid(row=5,column=1)

#Алерт с затраченным топливом




window.mainloop()