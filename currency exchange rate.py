from tkinter.messagebox import showerror

import requests
from tkinter import *
from tkinter import messagebox as mb




def exchange():
    code = e0.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/RUB')
            data = response.json()
            #print (data)
            if code in data['rates']:
                ex_rates=data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс к рублю {ex_rates}')
        except Exception as err:
            mb,showerror('ERROR!',err)
    else:
        mb.showwarning('','Выберете вылюту')


w = Tk()
w.geometry('600x400')

Label(text='Введите код валюты').pack(pady = (10,0))
e0 = Entry();e0.pack(pady = (10,0))

Button(text='Получить курс', command=exchange).pack(pady = (10,0))


w.mainloop()

#result = requests.get('https://open.er-api.com/v6/latest/USD')
#print(result)