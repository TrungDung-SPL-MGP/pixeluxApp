import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import askokcancel, showinfo, WARNING,showerror
import ttkbootstrap as ttk
import mysql.connector
from mysql.connector import Error


def get_size_names():
    try:
        connection =mysql.connector.connect(
            host='localhost',
            user='root',
            password='041199',
            database='pixeluxApp')
        c=connection.cursor()
        sql_query=("SELECT name FROM size")
        c.execute(sql_query)
       
        sizes=c.fetchall()
        size_name_list=[size[0] for size in sizes]
        return size_name_list    

        
    except mysql.connector.Error as error:
        showerror("Error","Error")
    finally:
        if connection.is_connected():
            c.close()
            connection.close()
            print("Connect database close")

def get_size_info(size_name):
    try:
        connection =mysql.connector.connect(
            host='localhost',
            user='root',
            password='041199',
            database='pixeluxApp')
        c=connection.cursor()
        sql_query=("SELECT width,height FROM size WHERE name=%s")
        c.execute(sql_query,(size_name,))
       
        sizes=c.fetchone()
        return sizes
    except mysql.connector.Error as error:
        showerror("Error","Error")
    finally:
        if connection.is_connected():
            c.close()
            connection.close()
            print("Connect database close")

def show_size(event):
    selected_size=cbSize.get()
    sizes=get_size_info(selected_size)
    if sizes:
        width,height=sizes
        entry_size_width.delete(0,END)
        entry_size_width.insert(0,width)
        entry_size_height.delete(0,END)
        entry_size_height.insert(0,height)
    else:
        print("Note size")    
root =ttk.Window(themename="darkly")
root.title('App v1.0')

frameSize = ttk.Frame(root,)
frameSize.grid(row=0,column=0)
lbSize=ttk.Label(master=frameSize,text="Choose Size")
lbSize.grid(row=0,column=0,padx=5,pady=5)
cbSize=ttk.Combobox(master=frameSize,width=100,state="readonly")
cbSize.grid(row=0,column=1,padx=5,pady=5)
size_names=get_size_names()

cbSize['values']=size_names

label_width=ttk.Label(master=frameSize,text="Width")
label_width.grid(row=1,column=0,padx=5,pady=5)
entry_size_width=ttk.Entry(master=frameSize,width=100)
entry_size_width.grid(row=1,column=1,padx=5,pady=5)
label_height=ttk.Label(master=frameSize,text="Height")
label_height.grid(row=2,column=0,padx=5,pady=5)
entry_size_height=ttk.Entry(master=frameSize,width=100)
entry_size_height.grid(row=2,column=1,padx=5,pady=5)
cbSize.bind("<<ComboboxSelected>>",show_size)
root.mainloop()