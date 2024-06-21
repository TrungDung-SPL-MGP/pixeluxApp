import os
import tkinter as tk
from tkinter import Image, font
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
import mysql.connector
from PIL import Image, ImageTk
connection =mysql.connector.connect(host='localhost',user='root',password='041199',database='pixeluxApp')
c= connection.cursor()
def _init_text():
    entry_x_text.delete(0,END)
    entry_y_text.delete(0,END)
    entry_width_text.delete(0,END)
    entry_height_text.delete(0,END)
    entry_data_text.delete(0,END)
    cbSize.delete(0,END)
    cbFont.delete(0,END)
    
def add_text():
    global text_img, rect, t_size, t_font, text_style,start_x, start_y  
    
    t_name = entry_name_text.get()
    x = int(entry_x_text.get())
    y = int(entry_y_text.get())
    t_width = int(entry_width_text.get())
    t_height = int(entry_height_text.get())
    t_data = entry_data_text.get()
    t_font = cbFont.get()
    t_size = cbSize.get()

    x1 = x + t_width
    y1 = y + t_height
    bg_color = color_var.get()

    rect = canvas.create_rectangle(x, y, x1, y1, fill=bg_color)
    fg_color = color_var_t.get()
    text_x = (x + x1) / 2
    text_y = (y + y1) / 2

    text_img = canvas.create_text(text_x, text_y, text=t_data, fill=fg_color, font=(t_font, t_size, text_style), anchor="center")
    canvas.itemconfig(text_img, font=(t_font, t_size, text_style), width=t_width)
    _init_text() 
    canvas.tag_bind(rect, "<ButtonPress-1>", start_drag)
    canvas.tag_bind(rect, "<B1-Motion>", drag)
       
    


def start_drag(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def drag(event):
    global last_x, last_y
    new_x = event.x
    new_y = event.y
    
    # Calculate the difference between current and last mouse positions
    dx = new_x - last_x
    dy = new_y - last_y
    
    # Move the QR code by the calculated difference
    canvas.move(rect, dx, dy)
    
    last_x = new_x
    last_y = new_y
    
    # Update x and y entry fields
    entry_x_text.delete(0, tk.END)
    entry_x_text.insert(0, str(new_x))
    entry_y_text.delete(0, tk.END)
    entry_y_text.insert(0, str(new_y))
def align_update():
    global text_style
    text_style=""
    if b_var.get():
        text_style+="bold "
    if i_var.get():
        text_style+="italic "
    if u_var.get():
        text_style+="underline "  
    canvas.itemconfig(text_img,font=(t_font,t_size,text_style))   
def align_t(align):
    if align=="left":
        canvas.itemconfig(text_img,anchor="se")
    elif align=="right":
        canvas.itemconfig(text_img,anchor="sw")
    elif align=="center":
        canvas.itemconfig(text_img,anchor="s")                   
def add_image():
    file_path =filedialog.askopenfilename(initialdir=os.getcwd(),title="Choose Image",filetypes=(("Image files","*.jpg *jpeg *.png *.gif"),("All file","*.*")))
    if file_path:
        image_name=os.path.basename(file_path)
        destination ="assets/images/photobackground/"+image_name
        try:
            os.makedirs(os.path.dirname(destination),exist_ok=True)
            os.rename(file_path,destination)

            spl= "INSERT INTO images_bg (nameimage,file_path) VALUE(%s,%s)"
            val=(image_name,destination)
            c.execute(spl,val)
            connection.commit()
            messagebox.showinfo("Success","Image added successfully")
        except:
            messagebox.showerror("Error","Image not added")
def update_text():
    pass

def delete_text():
    pass
def seach_text():
    pass
def submitText():
    messagebox.showinfo(title="Text fields",message="New text fields ")
def submitPicture():
    messagebox.showinfo(title="Picture fields",message="New picture fields ")    
def submitQrcode():
    messagebox.showinfo(title="Qr Code fields",message="New Qr code fields ")
def submitBarcode():
    messagebox.showinfo(title="Bar code fields",message="New Bar code fields ")
def get_size_names():
    
        
        sql_query=("SELECT name FROM size")
        c.execute(sql_query)
       
        sizes=c.fetchall()
        size_name_list=[size[0] for size in sizes]
        return size_name_list    

        
    

def get_size_info(size_name):
    
       
        sql_query=("SELECT width,height FROM size WHERE name=%s")
        c.execute(sql_query,(size_name,))
       
        sizes=c.fetchone()
        return sizes
    

def show_size(event):
    selected_size=cbSizeTable.get()
    sizes=get_size_info(selected_size)
    if sizes:
        width,height=sizes
        entry_size_width.delete(0,END)
        entry_size_width.insert(0,width)
        entry_size_height.delete(0,END)
        entry_size_height.insert(0,height)
    else:
        print("Note size")  
def get_background_names():
    try:
        
        sql_query=("SELECT nameimage FROM images_bg")
        c.execute(sql_query)
       
        images=c.fetchall()
        image_bg_name_list=[image_bg[1] for image_bg in images]
        return image_bg_name_list    

        
    except mysql.connector.Error as error:
        messagebox.showerror("Error","Error")
    finally:
        if connection.is_connected():
            c.close()
            connection.close()
            print("Connect database close")

def get_background_info(image_bg_name):
    try:
       
        sql_query=("SELECT * FROM images_bg WHERE nameimage=%s")
        c.execute(sql_query,(image_bg_name,))
       
        images_bg=c.fetchone()
        return images_bg
    except mysql.connector.Error as error:
        messagebox.showerror("Error","Error")
    finally:
        if connection.is_connected():
            c.close()
            connection.close()
            print("Connect database close")


def show_background(event):
    selected_background=cbBackGround.get()
    imgaes_background=get_background_info(selected_background)
    if imgaes_background:
        nameimage=imgaes_background
        
    else:
        print("Note size")         
def fontcolor():#font color
    color = colorchooser.askcolor()[1]
    color_var_t.set(color)

    print(color)
def backgroundcolor():#font color
    color = colorchooser.askcolor()[1]
    color_var.set(color)
def alignI():#font color
    current_font=entry_data_text.cget("italic")
    if "bold" in current_font:
        new_font=current_font.replace("italic","")
    else:
        new_font=current_font+"italic"
    entry_data_text(font=new_font)  
def alignB():#font color
    current_font=entry_data_text.cget("font")
    if "bold" in current_font:
        new_font=current_font.replace("bold","")
    else:
        new_font=current_font+"bold"
    entry_data_text(font=new_font)           
def alignU():#font color
    current_font=entry_data_text.cget("underline")
    if "bold" in current_font:
        new_font=current_font.replace("underline","")
    else:
        new_font=current_font+"underline"
    entry_data_text(font=new_font)  
def alignLeft():
    messagebox.showinfo(title="Align",message="Align Left")
def alignRight():
    messagebox.showinfo(title="right",message="Right")
def alignCenter():
    messagebox.showinfo(title="Align",message="Align Center")
def changeFont(evevt):
    selectFont=cbFont.get()
    selectSize=cbSize.get()
    

def updateSizeTemplate():
    selectSize=cbSizeTable.get()
    if selectSize=="Custom":
        canvas.config(width=int(canvas_width.get()),height=int(canvas_height.get())) 
    else:
        width,height=map(int,selectSize.split("x"))
        canvas.config(width=width,height=height)


      
root=ttk.Window(themename="litera")
root.title('Text manager')
root.geometry("1920x1000")
root.minsize(400,250)
root.maxsize(1920,1080)

#Photo
photoSave = PhotoImage(file="assets/images/save/Web/1.png")
photoReview = PhotoImage(file="assets/images/eye/Web/1.png")
photoLeft=PhotoImage(file="assets/images/left/Web/1.png")
photoRight=PhotoImage(file="assets/images/right/Web/1.png")
photo123=PhotoImage(file="assets/images/123/Web/1.png")
photoCenter=PhotoImage(file="assets/images/center/Web/1.png")
photobgFont=PhotoImage(file="assets/images/bgFont/Web/1.png")
photofgFont=PhotoImage(file="assets/images/fgFont/Web/1.png")
photoB=PhotoImage(file="assets/images/b/Web/1.png")
photoI=PhotoImage(file="assets/images/i/Web/1.png")
photoU=PhotoImage(file="assets/images/u/Web/1.png")
photoService=PhotoImage(file="assets/images/service/Web/1.png")
photoPicture=PhotoImage(file="assets/images/picture/Web/1.png")
photoUpload=PhotoImage(file="assets/images/photobackground/upload.png")
#option font
optitonfont=["Arial","Helvetica","Time new roman",""]
#option size

#option color

#option background
#text parameter
entry_x_text=tk.IntVar()
entry_y_text=tk.IntVar()
entry_width_text=tk.IntVar()
entry_height_text=tk.IntVar()
entry_data_text=tk.StringVar()
#text parameter
entryX=tk.IntVar()
entryY=tk.IntVar()
entryWidth=tk.IntVar()
entryHeight=tk.IntVar()
#picture parameter
entryXPicture=tk.IntVar()
entryYPicture=tk.IntVar()
entryWidthPicture=tk.IntVar()
entryHeightPicture=tk.IntVar()
canvas_width=tk.StringVar()
canvas_height=tk.StringVar()
entryText=tk.StringVar()
entryText.set("Text review")
font_families=font.families()
cbSizeTable=tk.StringVar()
cbSizeTable.set("1280x720")
cbSizeTable=tk.StringVar()
cbSizeTable.set("1200x640")
cbSize=tk.StringVar()
cbSize.set("12")
cbColor=tk.StringVar()
cbColor.set("Black")
cbBackGround=tk.StringVar()
cbBackGround.set("White")
#qrcode parameter
entryXqrcode=tk.IntVar()
entryYqrcode=tk.IntVar()
entryWidthqrcode=tk.IntVar()
entryHeightqrcode=tk.IntVar()
entryTextqrcode=tk.StringVar()
#barcode parameter
entryXbarcode=tk.IntVar()
entryYbarcode=tk.IntVar()
entryWidthbarcode=tk.IntVar()
entryHeightbarcode=tk.IntVar()
entryTextbarcode=tk.StringVar()
nameTemplate=tk.StringVar()
nameTemplate.set("Template")


#button
#fame
frame =ttk.Frame(master=root,border=1,relief=SUNKEN,width=800,height=580)
frame.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NW)

frameSevice =ttk.Frame(master=root,border=1,relief=SUNKEN,width=300,height=480)
frameSevice.grid(row=0,column=3,padx=10,pady=10,sticky=tk.NW)



labelTemplate=ttk.Label(master=frame,text='Template size (1200x640)',font=("arial",12),border=10,background='#f4f4f4')
labelTemplate.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
#frameMain
btnSave=ttk.Button(master=frame,text='Save Temp',width=10,image=photoSave,compound="left",style="secondary.TButton")
btnSave.grid(row=0,column=1,padx=5,pady=5,sticky=tk.E)
btnPreview=ttk.Button(master=frame,text='Preview',width=10,image=photoReview,compound='left',style="secondary.TButton")
btnPreview.grid(row=0,column=2,padx=5,pady=5)

#btnText=ttk.Button(master=frame,text='Text',width=8,command=submitText,style="secondary.TButton")
#btnText.grid(row=1,column=0,padx=5,pady=2,sticky=tk.W)
#btnPicture=ttk.Button(master=frame,text='Picture',width=8,command=submitPicture,style="secondary.TButton")
#btnPicture.grid(row=2,column=0,padx=5,pady=2,sticky=tk.W)
#btnQrCode=ttk.Button(master=frame,text='Qr Code',width=8,command=submitQrcode,style="secondary.TButton")
#btnQrCode.grid(row=3,column=0,padx=5,pady=2,sticky=tk.W)
#btnBarCode=ttk.Button(master=frame,text='Bar Code',width=8,command=submitBarcode,style="secondary.TButton")
#btnBarCode.grid(row=4,column=0,padx=5,pady=2,sticky=tk.W)
canvas=tk.Canvas(master=frame,width=1200,height=640,borderwidth=1,background="#fafafa",relief="solid")
canvas.grid(row=1,column=0,rowspan=12,columnspan=3,padx=5,pady=5,sticky=tk.SE)
                
#frameService
#frameServiveText
labelTitle =ttk.Label(master=frameSevice,text="PROPERTIES",
                      padding=5,
                      font=('Helvitica',12,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelNameText=ttk.Label(master=frameSevice,text="Name Fields",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelNameText.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
entry_name_text=ttk.Entry(master=frameSevice,width=10)
entry_name_text.grid(row=1,column=1,columnspan=3,sticky=tk.EW,padx=10,pady=10)
labelX=ttk.Label(master=frameSevice,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)
textX=tk.StringVar()
textX.set('0')
entry_x_text=ttk.Entry(master=frameSevice,width=10,textvariable=textX)
entry_x_text.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frameSevice,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)
textY=tk.StringVar()
textY.set('0')
entry_y_text=ttk.Entry(master=frameSevice,width=10,textvariable=textY)
entry_y_text.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)
textW=tk.StringVar()
textW.set('0')
labelWidth=ttk.Label(master=frameSevice,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entry_width_text=ttk.Entry(master=frameSevice,width=10,textvariable=textW)
entry_width_text.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frameSevice,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)
textH=tk.StringVar()
textH.set('0')
entry_height_text=ttk.Entry(master=frameSevice,width=10,textvariable=textH)
entry_height_text.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)

labelText=ttk.Label(master=frameSevice,text="Text",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelText.grid(row=4,column=0,padx=5,pady=5,sticky=tk.EW)
textT=tk.StringVar()
textT.set('Text review')
entry_data_text=ttk.Entry(master=frameSevice,width=20,textvariable=textT)
entry_data_text.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

labelFont=ttk.Label(master=frameSevice,text="Font Family",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelFont.grid(row=5,column=0,padx=5,pady=5,sticky=tk.EW)

cbFont=ttk.Combobox(master=frameSevice,width=15,state="readonly")
cbFont.grid(row=5,column=1,padx=5,pady=5,sticky=tk.W)
cbFont['value']=("Arial","Helvetica","Time New Roman")
cbFont.set("Arial")
cbFont.bind("<<ComboboxSelected>>",changeFont)

labelSize=ttk.Label(master=frameSevice,text="Size",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=5,column=2,padx=5,pady=5,sticky=tk.EW)

cbSize=ttk.Combobox(master=frameSevice,width=10)
cbSize.grid(row=5,column=3,padx=5,pady=5,sticky=tk.E)
cbSize['value']=("10","12","14","16","18","20","22","24","28","30","32","34","36","38","40","42","46","50","54","58","60","64","68","72","80","90","100")
cbSize.set("20")
cbSize.bind("<<ComboboxSelected>>",changeFont)
labelAlign=ttk.Label(master=frameSevice,text="Align",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=6,column=0,padx=5,pady=5,sticky=tk.EW)
btnAlignLeft =ttk.Button(master=frameSevice,image=photoLeft,style="secondary.outline.TButton",command=lambda: align_t("left"))
btnAlignLeft.grid(row=6,column=1,padx=5,pady=5,sticky=tk.W)
btnAlignRight =ttk.Button(master=frameSevice,image=photoRight,style="secondary.outline.TButton",command=lambda: align_t("right"))
btnAlignRight.grid(row=6,column=1,padx=5,pady=5,sticky=tk.E)
btnAlignCenter =ttk.Button(master=frameSevice,image=photoCenter,style="secondary.outline.TButton",command=lambda: align_t("center"))
btnAlignCenter.grid(row=6,column=1,padx=5,pady=5)


#btnAligJustify =ttk.Button(master=frameSevice,image=photo123,style="secondary.outline.TButton")
#btnAligJustify.grid(row=6,column=0,columnspan=2,padx=5,pady=5,sticky=tk.N)
b_var=tk.BooleanVar(master=frameSevice)
i_var=tk.BooleanVar(master=frameSevice)
u_var=tk.BooleanVar(master=frameSevice) 
btnAlignB =ttk.Checkbutton(master=frameSevice,image=photoB,variable=b_var,command=align_update)
btnAlignB.grid(row=6,column=2,columnspan=2,padx=15,pady=5,sticky=tk.W)
btnAlignI =ttk.Checkbutton(master=frameSevice,image=photoI,variable=i_var,command=align_update)
btnAlignI.grid(row=6,column=2,columnspan=2,padx=15,pady=5,sticky=tk.E)
btnAlignU =ttk.Checkbutton(master=frameSevice,image=photoU,variable=u_var,command=align_update)
btnAlignU.grid(row=6,column=2,columnspan=2,padx=5,pady=5)

labelAlign=ttk.Label(master=frameSevice,text="Font Color",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=7,column=2,columnspan=2,padx=5,pady=5,sticky=tk.W)


btnFontcolor =ttk.Button(master=frameSevice,image=photofgFont,style="secondary.outline.TButton",command=fontcolor)
btnFontcolor.grid(row=7,column=2,columnspan=2,padx=25,pady=5,sticky=tk.E)
color_var_t=tk.StringVar(master=frameSevice)
color_var_t.set("#000000")

labelAlign=ttk.Label(master=frameSevice,text="Background Color",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=7,column=0,columnspan=2,padx=5,pady=5,sticky=tk.W)

color_var=tk.StringVar(master=frameSevice)
btnBgColor =ttk.Button(master=frameSevice,image=photobgFont,style="secondary.outline.TButton",command=backgroundcolor)
btnBgColor.grid(row=7,column=0,columnspan=2,padx=25,pady=5,sticky=tk.E)
color_var.set("#ffffff")

#button service
btnAddText=ttk.Button(master=frameSevice,text="Add",style=("secondary.TButton"),width=6,command=add_text)
btnAddText.grid(row=8,column=0,padx=5,pady=10,sticky=tk.E)

btnEditText=ttk.Button(master=frameSevice,text="Edit",style=("secondary.TButton"),width=6,command=update_text)
btnEditText.grid(row=8,column=1,padx=15,pady=10)

btnDeleteText=ttk.Button(master=frameSevice,text="Delete",style=("secondary.TButton"),width=6,command=delete_text)
btnDeleteText.grid(row=8,column=2,padx=5,pady=10,sticky=tk.W)

btnSeachText=ttk.Button(master=frameSevice,text="Seach",style=("secondary.TButton"),width=6,command=seach_text)
btnSeachText.grid(row=8,column=3,padx=5,pady=10,sticky=tk.E)
#canvas.create_rectangle((0,0),(640,400),fill="#a0a0a0")
#
#frameInterface
frameInterface =ttk.Frame(master=root,border=1,relief=SUNKEN,width=600,height=300)
frameInterface.grid(row=1,column=0,padx=10,pady=10,sticky=tk.NW)
labelTitleInterface=ttk.Label(master=frameInterface,
                     text="TEMPHLATE PROPERTIES",
                     image=photoService,
                     compound='left',
                     padding=5,
                     font=('Helvitica',12,"bold"),
                     background='#f4f4f4',
                     width=50)
labelTitleInterface.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.W)

entryName=ttk.Entry(master=frameInterface,width=50,textvariable=nameTemplate)
entryName.grid(row=1,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

lebleNameTemplate=ttk.Label(master=frameInterface,text="Name template",
                            font=('Helvitica',8,"bold"),
                            background='#f4f4f4',
                            
                            )
lebleNameTemplate.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)

lebleNameTemplate=ttk.Label(master=frameInterface,text="Sceen type",
                            font=('Helvitica',8,"bold"),
                            background='#f4f4f4',
                            
                            )
lebleNameTemplate.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
cbSizeT=tk.StringVar()
cbSizeT=tk.StringVar()

cbSizeTable=ttk.Combobox(master=frameInterface,
                        state="readonly")

cbSizeTable.grid(row=2,column=1,columnspan=2,padx=5,pady=5,sticky=tk.EW)
size_names=get_size_names()

cbSizeTable['values']=size_names
cbSizeTable.current(0)


labelWidthT=ttk.Label(master=frameInterface,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidthT.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)

entry_size_width=ttk.Entry(master=frameInterface,width=10)
entry_size_width.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)

labelHeightT=ttk.Label(master=frameInterface,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeightT.grid(row=3,column=2,padx=5,pady=5,sticky=tk.W)

entry_size_height=ttk.Entry(master=frameInterface,width=10)
entry_size_height.grid(row=3,column=3,padx=5,pady=5,sticky=tk.W)
cbSizeTable.bind("<<ComboboxSelected>>",show_size)

btnUpdataSizeTemplate =ttk.Button(master=frameInterface,text="Update",image=photoUpload,compound="left",style="secondary.outline.TButton",command=updateSizeTemplate)
btnUpdataSizeTemplate.grid(row=2,column=3,padx=25,pady=5,sticky=tk.E)

labelAddBackground=ttk.Label(master=frameInterface,text="Add BackGround",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAddBackground.grid(row=4,column=2,padx=5,pady=5,sticky=tk.W)

btnFileBackGround =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=add_image)
btnFileBackGround.grid(row=4,column=3,padx=5,pady=5,sticky=tk.W)

labelAddPicture=ttk.Label(master=frameInterface,text="Add Picture",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAddPicture.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

btnPictureFile =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=fontcolor)
btnPictureFile.grid(row=4,column=1,padx=5,pady=5,sticky=tk.W)

lebleChooseBackground=ttk.Label(master=frameInterface,text="Chose Background",
                            font=('Helvitica',8,"bold"),
                            background='#f4f4f4',
                            
                            )
lebleChooseBackground.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

cbBackGround=ttk.Combobox(master=frameInterface)
cbBackGround.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
cbBackGround.bind("<<ComboboxSelected>>",show_background)
#frameCode
frameCode =ttk.Frame(master=root,border=1,relief=SUNKEN,width=600,height=300)
frameCode.grid(row=1,column=1,padx=10,pady=10,sticky=tk.NW)

labelTitleCode=ttk.Label(master=frameCode,
                        text="Inteface Data",
                        font=('Helvitica',12,'bold'),
                        padding=5,
                        background='#f4f4f4',
                        image=photoService,
                        compound='left',
                        width=50

                        
                        )
labelTitleCode.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.W)
labelHeightC=ttk.Label(master=frameCode,text="SouceCode:",padding=5,font=('Helvitica',10,"bold"),background='#f4f4f4',width=max)
labelHeightC.grid(row=1,column=0,padx=5,pady=5,sticky=tk.E)
textCode=tk.Text(master=frameCode,width=30,height=4)
textCode.grid(row=2,column=1,columnspan=3,padx=5,pady=5,sticky=tk.W)
#frameOutput

#frameHelp

#frameAbout
scrollbar=tk.Scrollbar(root)
scrollbar.grid(row=0,column=4,rowspan=2,sticky=tk.NS)





root.mainloop()