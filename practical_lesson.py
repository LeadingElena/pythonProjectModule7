import tkinter
import os
from os.path import basename

from tkinter import *
from tkinter import filedialog, messagebox


def file_select():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '.*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

def info_click():
    messagebox.showinfo('Info', 'Для открытия файла необходимо в проводнике найти и выбрать нужный файл.')

def about_click():
    messagebox.showinfo('О программе', 'Автор: Федорова Елена\nВерсия: 1.1')

window = tkinter.Tk()
window.title('Проводник')
window.geometry('550x150')
window.resizable(False, False)

menu = Menu()
menu.add_cascade(label='Инфо', command=info_click)
menu.add_cascade(label='О программе', command=about_click)
window.config(menu=menu)

text = tkinter.Label(window, text='Файл: ', height=5, width=80, background='#FFD39B', foreground='#00008B')
text.grid(column=1, row=1)

button_select = tkinter.Button(window, height=3, width=30, text='Выбрать файл', background='#7FFFD4',
                               foreground='#00008B', command=file_select)
button_select.grid(ipadx=10, column=1, row=2)

window.mainloop()