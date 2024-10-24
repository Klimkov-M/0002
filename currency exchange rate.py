import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb




def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/RUB')
            data = response.json()
            #print (data)
            if code in data['rates']:
                ex_rates=data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс к рублю {ex_rates}')
        except Exception as err:
            mb.showerror('ERROR!',err)
    else:
        mb.showwarning('','Выберете вылюту')


pop_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]

w = Tk()
w.geometry('600x400')

Label(text='Введите код валюты').pack(pady = (10,0))
combobox = ttk.Combobox(values=pop_cur);combobox.pack(pady = (10,0))

ttk.Button(text='Получить курс', command=exchange).pack(pady = (10,0))


w.mainloop()

#result = requests.get('https://open.er-api.com/v6/latest/USD')
#print(result)