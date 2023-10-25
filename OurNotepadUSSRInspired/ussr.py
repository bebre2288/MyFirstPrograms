from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter.ttk import Radiobutton 
from PIL import Image, ImageTk
import os
import time
import webbrowser
import sys
#window options
window = Tk()
window.geometry('550x475')
window.title("НАШ блокнот")
window.resizable(False, False)
#antirobbersys
def b1(event):
    print("axaxaxxaxaxxa")
    webbrowser.open_new_tab('https://vk.com/inator3000')
    messagebox.showinfo('', 'АВТОРЫ:sashkagolem@gmail.com & jjjj92973@gmail.com')
def b2(event):
    print("xxa")
    window.destroy()
#save options
def save():
    files = [('text Document', '*.txt')]
    perry = asksaveasfile(filetypes = files, defaultextension = files)
    s = txt.get(1.0, END)
    perry.write(s)
    perry.close()
#save options by button
def b3():
    files = [('text Document', '*.txt')]
    perry = asksaveasfile(filetypes = files, defaultextension = files)
    s = txt.get(1.0, END)
    perry.write(s)
    perry.close()
    print('sssssss')
def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)
#messagebox of clearing scrollbox
def clicked():
    res = messagebox.askquestion('предупреждение', 'очистить всё?')
    if res=='yes':
        txt.delete(1.0, END)
#open txt file
def open_file():
    # global file
    file_name = filedialog.askopenfilename()
    file = open(file_name, 'r')
    # global file_content
    file_content = file.read();
    print (file_content)
    txt.insert('1.0',file_content)
#txt colour
def black():
    print('black')
    txt.configure(fg="#000000")
def red():
    print('red')
    txt.configure(fg="#ff5555")
def dark_blue():
    print('dark_blue')
    txt.configure(fg="#00008B")
def white():
    print('white')
    txt.configure(fg="#FFFFFF")
#txt type
def calibr():
    print('Calibri 12')
    txt.configure(font="Calibri 12")
    txt.configure(width=45, height=20)
def ari():
    print("Arial 12")
    txt.configure(font="Arial 12")
    txt.configure(width=40, height=21)
def gaud():
    print('Gadugi 12')
    txt.configure(font="Gadugi 12")
    txt.configure(width=40, height=20)
def georg():
    print('Georgia 12')
    txt.configure(font="Georgia 12")
    txt.configure(width=35, height=21)
#image load
image_file = Image.open(resource_path("1200.gif"))
bg_image = ImageTk.PhotoImage(image_file)
#ignore this part
canvas_area = Canvas(window, width=700, height=500, background="#99eebb")
canvas_area.place(x='0',y='0') 
bg=Label(canvas_area,image=bg_image)
bg.pack()
#text input(scrolltext)
txt = scrolledtext.ScrolledText(canvas_area, width=50, height=25)
txt.focus()
txt.place(x='125',y='35');
#clear button
btn = Button(canvas_area, text="очистить", command=clicked)
btn.place(x='300',y='440')
#button save
btn2 = Button(canvas_area, text = 'сохранить', command = lambda : save())
btn2.place(x='400',y='440')
#button open
btn3 = Button(canvas_area, text = 'открыть', command=open_file)
btn3.place(x='200',y='440')
#menu
main_menu = Menu(window)
window.config(menu=main_menu)
menu_item01 = Menu(main_menu) 
menu_item01 = Menu(main_menu, tearoff=0)
menu_item01_submenu01 = Menu(menu_item01, tearoff=0)
menu_item01_submenu01.add_command(label="чёрный",command=black)
menu_item01_submenu01.add_command(label='красный',command=red) 
menu_item01_submenu01.add_command(label='синий',command=dark_blue) 
menu_item01_submenu01.add_command(label='белый',command=white) 
menu_item01.add_cascade(label='цвет текста', menu=menu_item01_submenu01)  
main_menu.add_cascade(label='Настройки', menu=menu_item01)  
menu_item01.add_separator() 
menu_item01_submenu01 = Menu(menu_item01, tearoff=0)
menu_item01_submenu01.add_command(label="Calibri 12",command=calibr)
menu_item01_submenu01.add_command(label='Arial 12',command=ari) 
menu_item01_submenu01.add_command(label='Gadugi 12',command=gaud) 
menu_item01_submenu01.add_command(label='Georgia 12',command=georg) 
menu_item01.add_cascade(label='шрифт', menu=menu_item01_submenu01)  
#смэрть ворам
window.bind('<Shift-Control-Return>', b1)
window.bind('<Escape>', b2)
window.bind('<Control-Tab>', b3)
window.mainloop()
