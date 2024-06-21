import tkinter as tk
from tkinter import font
import qrcode
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
from PIL import Image, ImageTk
from model.m_photo import Photo
def change_color():
    colorchooser.askcolor()[0]

def clear_qr_code():
    pass    
    
def generate_qr_code():
    link = entryLinkQrcode.get()
    
    x = int(entry_x_qr.get())
    
    
    y = int(entry_y_qr.get())

    # Tạo mã QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Create QR
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    
    qr_img = ImageTk.PhotoImage(qr_img)
    
    # Hiển thị hình ảnh trên Canvas tại vị trí được chỉ định
    canvas.create_image(x, y, anchor=tk.NW, image=qr_img)
    canvas.image = qr_img


class QRCodeField:
    def __init__(self,id,x,y,width,height,name,value,bg_color,color,bg_img):
       self.id = id
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.name = name
       self.value = value
       self.bg_color = bg_color
       self.color = color
       self.bg_img = bg_img
    def get_id(self):
        return self.id 
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y=y
    def get_y(self):
        return self.y
    def set_width(self,width):
        self.width=width
    def get_width(self):
        return self.width
    def set_height(self,height):
        self.height=height
    def get_height(self):
        return self.height
    def set_value(self,value):
        self.value=value
    def get_value(self):
        return self.value
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_bg_color(self,bg_color):
        self.bg_color=bg_color

    def get_bg_color(self):
        return self.bg_color
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_bg_img(self,bg_img):
        self.bg_img=bg_img
    def get_bg_img(self):
        return self.bg_img
root=ttk.Window(themename="litera") 
frameSevice =ttk.Frame(master=root)   
labelTitle =ttk.Label(master=frameSevice,text="PROPERTIES",
                      padding=5,
                      font=('Helvitica',12,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=Photo.photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelSettingbase=ttk.Label(master=frameSevice,text="SETTING BASE",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelSettingbase.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

frameSevice =ttk.Frame()
labelX=ttk.Label(master=frameSevice,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)

entry_x_qr=ttk.Entry(master=frameSevice,width=10)
entry_x_qr.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frameSevice,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)

entry_y_qr=ttk.Entry(master=frameSevice,width=10)
entry_y_qr.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)

labelWidth=ttk.Label(master=frameSevice,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entryWidth=ttk.Entry(master=frameSevice,width=10)
entryWidth.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frameSevice,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)

entryHeight=ttk.Entry(master=frameSevice,width=10)
entryHeight.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelSize=ttk.Label(master=frameSevice,text="Link",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

entryLinkQrcode=ttk.Entry(master=frameSevice,width=10)
entryLinkQrcode.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

btncolorQR=ttk.Button(master=frameSevice,text="Choese a Color",command=change_color)
btncolorQR.grid(row=5,column=0)

generate_button = ttk.Button(master=frameSevice, text="Generate QR Code", command=generate_qr_code,style="secondary.TButton")
generate_button.grid(row=6,column=0,columnspan=2)

clear_button = ttk.Button(master=frameSevice, text="Clear QR Code", command=clear_qr_code,style="secondary.TButton")
clear_button.grid(row=6,column=2,columnspan=2)

           
root.mainloop()
        