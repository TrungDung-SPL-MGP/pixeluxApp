import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
def generate_barcode():

    global barcode_img_tk,barcode_id
    data = entryLinkBarcode.get()
    x = int(entry_x_barcode.get())
    y = int(entry_y_barcode.get())
    # create barcode
    barcode_class = barcode.get_barcode_class('code39')  #'code128'
    barcode_instance = barcode_class(data, writer=ImageWriter())
    barcode_img = barcode_instance.render()

    barcode_img = ImageTk.PhotoImage(barcode_img)

    
    barcode_id=canvas.create_image(x, y, anchor=tk.NW, image=barcode_img)
    canvas.image = barcode_img

    canvas.tag_bind(barcode_id, "<ButtonPress-1>", start_drag)
    canvas.tag_bind(barcode_id, "<B1-Motion>", drag)
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
    canvas.move(barcode_id, dx, dy)
    
    last_x = new_x
    last_y = new_y
    
    # Update x and y entry fields
    entry_x_barcode.delete(0, tk.END)
    entry_x_barcode.insert(0, str(new_x))
    entry_y_barcode.delete(0, tk.END)
    entry_y_barcode.insert(0, str(new_y)) 
def clear_barcode():
    response = messagebox.askyesno("Clear Barcode", "Are you sure you want to clear the barcode?")

    if response:
        canvas.delete("all")
def submitText():
    messagebox.showinfo(title="Text fields",message="New text fields ")
def submitPicture():
    messagebox.showinfo(title="Picture fields",message="New picture fields ")    
def submitQrcode():
    messagebox.showinfo(title="Qr Code fields",message="New Qr code fields ")
def submitBarcode():
    messagebox.showinfo(title="Bar code fields",message="New Bar code fields ")

def fontcolor():#font color
    color = tk.colorchooser.askcolor()
    print(color)
def backgroundcolor():#font color
    color = tk.colorchooser.askcolor()
    print(color)
def alignI():#font color
    messagebox.showinfo(title="Align",message="Align I")
def alignB():#font color
    messagebox.showinfo(title="Align",message="Align B")    
def alignU():#font color
    messagebox.showinfo(title="Align",message="Align U")
def alignLeft():
    messagebox.showinfo(title="Align",message="Align Left")
def alignRight():
    messagebox.showinfo(title="right",message="Right")
def alignCenter():
    messagebox.showinfo(title="Align",message="Align Center")

def updateSizeTemplate():
    selectSize=cbSizeTable.get()
    if selectSize=="Custom":
        canvas.config(width=int(canvas_width.get()),height=int(canvas_height.get())) 
    else:
        width,height=map(int,selectSize.split("x"))
        canvas.config(width=width,height=height)


      
root=ttk.Window(themename="litera")
root.title('Text manager')
root.geometry("1280x720")
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
entryX=tk.IntVar()

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
frame.grid(row=0,column=0,padx=10,pady=10,sticky=tk.NW)

frameSevice =ttk.Frame(master=root,border=1,relief=SUNKEN,width=300,height=480)
frameSevice.grid(row=0,column=1,padx=10,pady=10,sticky=tk.NW)



labelTemplate=ttk.Label(master=frame,text='Template size (1200x640)',font=("arial",12),border=10,background='#f4f4f4')
labelTemplate.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
#frameMain
btnSave=ttk.Button(master=frame,text='Save Temp',width=10,image=photoSave,compound="left",style="secondary.TButton")
btnSave.grid(row=0,column=2,padx=5,pady=5,sticky=tk.E)
btnPreview=ttk.Button(master=frame,text='Preview',width=10,image=photoReview,compound='left',style="secondary.TButton")
btnPreview.grid(row=0,column=2,padx=5,pady=5)

btnText=ttk.Button(master=frame,text='Text',width=8,command=submitText,style="secondary.TButton")
btnText.grid(row=1,column=0,padx=5,pady=2,sticky=tk.W)
btnPicture=ttk.Button(master=frame,text='Picture',width=8,command=submitPicture,style="secondary.TButton")
btnPicture.grid(row=2,column=0,padx=5,pady=2,sticky=tk.W)
btnQrCode=ttk.Button(master=frame,text='Qr Code',width=8,command=submitQrcode,style="secondary.TButton")
btnQrCode.grid(row=3,column=0,padx=5,pady=2,sticky=tk.W)
btnBarCode=ttk.Button(master=frame,text='Bar Code',width=8,command=submitBarcode,style="secondary.TButton")
btnBarCode.grid(row=4,column=0,padx=5,pady=2,sticky=tk.W)
canvas=tk.Canvas(master=frame,width=640,height=400,borderwidth=1,background="#fafafa",relief="solid" )
canvas.grid(row=1,column=1,rowspan=12,columnspan=2,padx=5,pady=5,sticky=tk.SE)

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

labelSettingbase=ttk.Label(master=frameSevice,text="SETTING BASE",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelSettingbase.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelX=ttk.Label(master=frameSevice,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)
textX=tk.StringVar()
textX.set('0')
entry_x_barcode=ttk.Entry(master=frameSevice,width=10,textvariable=textX)
entry_x_barcode.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frameSevice,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)
textY=tk.StringVar()
textY.set('0')
entry_y_barcode=ttk.Entry(master=frameSevice,width=10,textvariable=textY)
entry_y_barcode.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)
textW=tk.StringVar()
textW.set('0')
labelWidth=ttk.Label(master=frameSevice,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entryWidth=ttk.Entry(master=frameSevice,width=10,textvariable=textW)
entryWidth.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frameSevice,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)
textH=tk.StringVar()
textH.set('0')
entryHeight=ttk.Entry(master=frameSevice,width=10,textvariable=textH)
entryHeight.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelSize=ttk.Label(master=frameSevice,text="Link",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

entryLinkBarcode=ttk.Entry(master=frameSevice,width=10)
entryLinkBarcode.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

generate_button = tk.Button(master=frameSevice, text="Generate Barcode", command=generate_barcode)
generate_button.grid(row=5,column=0,columnspan=2)

clear_button = tk.Button(master=frameSevice, text="Clear Barcode", command=clear_barcode)
clear_button.grid(row=5,column=1,columnspan=2)






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
cbSizeT.set('1200x640')
cavasSize=["800x480","1200x640","1000x600","Custom"]
cbSizeTable=ttk.Combobox(master=frameInterface,
                         values=cavasSize,textvariable=cbSizeT,state="readonly")
cbSizeTable.current(0)
cbSizeTable.grid(row=2,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

labelWidthT=ttk.Label(master=frameInterface,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidthT.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)

entryWidthT=ttk.Entry(master=frameInterface,width=10,textvariable=canvas_width)
entryWidthT.grid(row=3,column=0,padx=5,pady=5,sticky=tk.E)

labelHeightT=ttk.Label(master=frameInterface,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeightT.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)

entryHeightT=ttk.Entry(master=frameInterface,width=10,textvariable=canvas_height)
entryHeightT.grid(row=3,column=1,padx=5,pady=5,sticky=tk.E)

btnAlignU =ttk.Button(master=frameInterface,text="Update",image=photoUpload,compound="left",style="secondary.outline.TButton",command=updateSizeTemplate)
btnAlignU.grid(row=3,column=2,padx=25,pady=5,sticky=tk.E)

labelAlign=ttk.Label(master=frameInterface,text="Add BackGround",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=4,column=2,columnspan=2,padx=5,pady=5,sticky=tk.W)

btnAlignU =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=fontcolor)
btnAlignU.grid(row=4,column=2,columnspan=2,padx=25,pady=5,sticky=tk.E)

labelAlign=ttk.Label(master=frameInterface,text="Add Picture",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky=tk.W)

btnAlignU =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=backgroundcolor)
btnAlignU.grid(row=4,column=0,columnspan=2,padx=25,pady=5,sticky=tk.E)

lebleChooseBackground=ttk.Label(master=frameInterface,text="Chose Background",
                            font=('Helvitica',8,"bold"),
                            background='#f4f4f4',
                            
                            )
lebleChooseBackground.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

cbBackGround=ttk.Combobox(master=frameInterface,
                         values=['bg.png','bg2.png'])
cbBackGround.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
#frameCode
frameCode =ttk.Frame(master=root,border=1,relief=SUNKEN,width=600,height=300)
frameCode.grid(row=1,column=1,padx=10,pady=10,sticky=tk.NW)

labelTitleCode=ttk.Label(master=frameCode,
                        text="Inteface Code",
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
scrollbar.grid(row=0,column=2,rowspan=2,sticky=tk.NS)





root.mainloop()