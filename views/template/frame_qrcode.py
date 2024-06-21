import tkinter as tk
from tkinter import font
import qrcode
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
from PIL import Image, ImageTk
import mysql.connector
def change_color():
   foreground_color= colorchooser.askcolor()[1]
   return foreground_color

    
def  on_entry_key_press(event):
    if event.keycode == 86 and event.state == 4:
        entry_data_qr.event_generate("<<Paste>>")
    elif event.keycode == 67 and event.state == 4:
        entry_data_qr.event_generate("<<Copy>>")    

def clear_qr_code():
    response = messagebox.askyesno("Clear Qr code", "Are you sure you want to clear the  Qr code?")

    if response:
        canvas.delete("all")


def generate_qr_code():
    global qr_img_tk, qr_id
    
    link = entry_data_qr.get()
    x = int(entry_x_qr.get())
    y = int(entry_y_qr.get())
    w=int(entry_width_qr.get())
    h=int(entry_height_qr.get())
    # Tạo mã QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=0.5,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Create QR
    foreground_color="#000000"
    background_color = "#f6f6f6"
    # Create QR
    qr_img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    qr_img = qr_img.resize((w,h))
    # Convert QR image to PhotoImage
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    
    # Hiển thị hình ảnh trên Canvas tại vị trí được chỉ định
    qr_id = canvas.create_image(x, y, anchor=tk.NW, image=qr_img_tk)
    
    # Bind mouse events to allow dragging
    canvas.tag_bind(qr_id, "<ButtonPress-1>", start_drag)
    canvas.tag_bind(qr_id, "<B1-Motion>", drag)

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
    canvas.move(qr_id, dx, dy)
    
    last_x = new_x
    last_y = new_y
    
    # Update x and y entry fields
    entry_x_qr.delete(0, tk.END)
    entry_x_qr.insert(0, str(new_x))
    entry_y_qr.delete(0, tk.END)
    entry_y_qr.insert(0, str(new_y)) 
import tkinter.messagebox as messagebox

def save_qr():
    try:
        x = int(entry_x_qr.get())
        y = int(entry_y_qr.get())
        width = int(entry_width_qr.get())
        height = int(entry_height_qr.get())
        name = entry_name_qr.get()
        data = entry_data_qr.get()

        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="041199",
            database="pixeluxApp"
        )
        cursor = conn.cursor()
        values = (x, y, width, height, name, data, 1,1 ) 
        # SQL query to insert QR code data into the table
        query = "INSERT INTO fields_qrcode (x_qrcode, y_qrcode, width_qrcode, height_qrcode, name, data, active, id_canvas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
         # Adjust 'active' and 'id_canvas' values accordingly
        
        # Execute the SQL query
        cursor.execute(query, values)
        
        # Commit changes to the database
        conn.commit()
        
        # Close database connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "QR code data saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save QR code data: {str(e)}")

def seach_qr():
    user_id=cbb_seach.get()
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="041199",
            database="pixeluxApp"
        )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fields_qrcode WHERE name=%s",(user_id,))
    cus=cursor.fetchone()

    clear_qr()

    entry_x_qr.insert(0,cus[1])
    entry_y_qr.insert(0,cus[2])
    entry_width_qr.insert(0,cus[3])
    entry_height_qr.insert(0,cus[4])
    entry_name_qr.insert(0,cus[5])
    entry_data_qr.insert(0,cus[6])
def clear_qr():
    entry_x_qr.delete(0,END,)
    entry_y_qr.delete(0,END)
    entry_width_qr.delete(0,END)
    entry_height_qr.delete(0,END)
    entry_name_qr.delete(0,END)
    entry_data_qr.delete(0,END)    
def change_bg_color():
   background_color = colorchooser.askcolor()[1]
   return background_color 

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
canvas=tk.Canvas(master=frame,width=640,height=400,borderwidth=1,background="#fafafa",relief="solid")
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

entry_x_qr=ttk.Entry(master=frameSevice,width=10)
entry_x_qr.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frameSevice,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)

entry_y_qr=ttk.Entry(master=frameSevice,width=10)
entry_y_qr.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)

labelWidth=ttk.Label(master=frameSevice,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entry_width_qr=ttk.Entry(master=frameSevice,width=10)
entry_width_qr.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frameSevice,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)

entry_height_qr=ttk.Entry(master=frameSevice,width=10)
entry_height_qr.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelLink=ttk.Label(master=frameSevice,text="Link",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelLink.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

entry_data_qr=ttk.Entry(master=frameSevice,width=10)
entry_data_qr.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
entry_data_qr.bind("<Key>",on_entry_key_press)
lbName = ttk.Label(master=frameSevice,text="Name",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
lbName.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

entry_name_qr=ttk.Entry(master=frameSevice,width=10)
entry_name_qr.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

btncolorQR=ttk.Button(master=frameSevice,text="Choese ",command=seach_qr,style="secondary.TButton")
btncolorQR.grid(row=6,column=0,padx=5,pady=5)

btnbgcolorQR=ttk.Button(master=frameSevice,text="Save",command=save_qr,style="secondary.TButton")
btnbgcolorQR.grid(row=6,column=1,padx=5,pady=5)
generate_button = ttk.Button(master=frameSevice, text="Generate", command=generate_qr_code,style="secondary.TButton")
generate_button.grid(row=6,column=2,padx=5,pady=5)

clear_button = ttk.Button(master=frameSevice, text="Clear ", command=clear_qr_code,style="secondary.TButton")
clear_button.grid(row=6,column=3,padx=5,pady=5 )

lbSeach = ttk.Label(master=frameSevice,text="Seach",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
lbSeach.grid(row=7,column=0,padx=5,pady=5,sticky=tk.W)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="041199",
    database="pixeluxApp"
)
cursor = connection.cursor()

# Execute SQL query to fetch image names
cursor.execute("SELECT name FROM fields_qrcode")
name_qr = [row[0] for row in cursor.fetchall()]

# Close cursor and connection
cursor.close()
connection.close()

cbb_seach=ttk.Combobox(master=frameSevice,values=name_qr)
cbb_seach.grid(row=7,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

cbb_seach.bind("<<ComboboxSelected>>",seach_qr)

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