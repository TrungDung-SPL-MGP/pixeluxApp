import os
import tkinter as tk
from tkinter import font
from tkinter import filedialog
import cv2
import qrcode
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage, messagebox,Frame
from tkinter  import colorchooser
import mysql.connector
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

    canvas.tag_bind(barcode_id, "<ButtonPress-1>", start_drag_barcode)
    canvas.tag_bind(barcode_id, "<B1-Motion>", drag_barcode)
def start_drag_barcode(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def drag_barcode(event):
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
    canvas.tag_bind(rect, "<ButtonPress-1>", start_drag_text)
    canvas.tag_bind(rect, "<B1-Motion>", drag_text)
       
    


def start_drag_text(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def drag_text(event):
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

def show_frame():
    for frame in frames:
        frame.grid_forget()
    selected_frame=radio_var.get()
    frames[selected_frame].grid(row=2,column=0,columnspan=4)
        
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
        messagebox.showerror("Error","Error")
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
        messagebox.showerror("Error","Error")
    finally:
        if connection.is_connected():
            c.close()
            connection.close()
            print("Connect database close")

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
def changeFont(evevt):
    selectFont=cbFont.get()
    entryText.config(font=(selectFont,cbSize))
def updateSizeTemplate():
    selectSize=cbSizeTable.get()
    if selectSize=="Custom":
        canvas.config(width=int(canvas_width.get()),height=int(canvas_height.get())) 
    else:
        width,height=map(int,selectSize.split("x"))
        canvas.config(width=width,height=height)
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
def choese_background_img():
    global img_bg,w_bg,h_bg,img_tk
    selected_image = cbBackGround.get()
    image_path = get_image_path(selected_image)

    if image_path:
        img_bg=Image.open(image_path)
        w_bg=int(entry_size_width.get())
        h_bg=int(entry_size_height.get())
        img_bg=img_bg.resize((w_bg,h_bg))
        img_tk=ImageTk.PhotoImage(img_bg)

        canvas.create_image(0,0,anchor=tk.NW,image=img_tk)
#imageFeidls
def display_image():
    global img_id,x,y
    selected_image = cbChoosePicture.get()
    image_path = get_image_path(selected_image)
    
    if image_path:
        # Load image from file
        img = Image.open(image_path)
        width_img=int(entry_width_img.get())
        height_img=int(entry_height_img.get())
        
        img = img.resize((width_img, height_img))
        
        # Convert image to PhotoImage
        img_tk = ImageTk.PhotoImage(img)
        x = int(entry_x_img.get())
        y = int(entry_y_img.get())
        # Display image on canvas
        img_id=canvas.create_image(x, y, anchor=tk.NW,image=img_tk)
        
        # Save a reference to the image to prevent it from being garbage collected
        canvas.image = img_tk
        canvas.tag_bind(img_id, "<ButtonPress-1>", start_drag_img)
        canvas.tag_bind(img_id, "<B1-Motion>", drag_img)
def get_image_path(selected_image):
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="041199",
        database="pixeluxApp"
    )
    cursor = connection.cursor()
    
    # Execute SQL query to fetch image path based on selected image name
    cursor.execute("SELECT file_path FROM images_bg WHERE nameimage = %s", (selected_image,))
    result = cursor.fetchone()
    
    # Close cursor and connection
    cursor.close()
    connection.close()
    
    # Return the image path
    return result[0] if result else None
def start_drag_img(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def drag_img(event):
    global last_x, last_y
    new_x = event.x
    new_y = event.y
    
    # Calculate the difference between current and last mouse positions
    dx = new_x - last_x
    dy = new_y - last_y
    
    # Move the QR code by the calculated difference
    canvas.move(img_id, dx, dy)
    
    last_x = new_x
    last_y = new_y
    
    # Update x and y entry fields
    entry_x_img.delete(0, tk.END)
    entry_x_img.insert(0, str(new_x))
    entry_y_img.delete(0, tk.END)
    entry_y_img.insert(0, str(new_y))
      
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
#frame =ttk.Frame(master=root,border=1,relief=SUNKEN,width=800,height=580)
#frame.grid(row=0,column=0,padx=10,pady=10,sticky=tk.NW)

#frameSevice =ttk.Frame(master=root,border=1,relief=SUNKEN,width=300,height=480)
#frameSevice.grid(row=0,column=1,padx=10,pady=10,sticky=tk.NW)
frame =ttk.Frame(master=root,border=1,relief=SUNKEN,width=800,height=580)
frame.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=tk.NW)

frameSevice =ttk.Frame(master=root,border=1,relief=SUNKEN,width=300,height=480)
frameSevice.grid(row=0,column=2,columnspan=2,padx=10,pady=10,sticky=tk.NW)



labelTemplate=ttk.Label(master=frame,text='Template size (1200x640)',font=("arial",12),border=10,background='#f4f4f4')
labelTemplate.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
#frameMain
btnSave=ttk.Button(master=frame,text='Save Temp',width=10,image=photoSave,compound="left",style="secondary.TButton")
btnSave.grid(row=0,column=1,padx=5,pady=5,sticky=tk.E)
btnPreview=ttk.Button(master=frame,text='Preview',width=10,image=photoReview,compound='left',style="secondary.TButton")
btnPreview.grid(row=0,column=2,padx=5,pady=5)

canvas=tk.Canvas(master=frame,width=1200,height=640,borderwidth=1,background="#fafafa",relief="solid")
canvas.grid(row=1,column=0,rowspan=12,columnspan=3,padx=5,pady=5,sticky=tk.SE)


#labelTemplate=ttk.Label(master=frame,text='Template size (1200x640)',font=("arial",12),border=10,background='#f4f4f4')
#labelTemplate.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
#frameMain
#btnSave=ttk.Button(master=frame,text='Save Temp',width=10,image=photoSave,compound="left",style="secondary.TButton")
#btnSave.grid(row=0,column=2,padx=5,pady=5,sticky=tk.E)
#btnPreview=ttk.Button(master=frame,text='Preview',width=10,image=photoReview,compound='left',style="secondary.TButton")
#btnPreview.grid(row=0,column=2,padx=5,pady=5)

#btnText=ttk.Button(master=frame,text='Text',width=8,command=submitText,style="secondary.TButton")
#btnText.grid(row=1,column=0,padx=5,pady=2,sticky=tk.W)
#btnPicture=ttk.Button(master=frame,text='Picture',width=8,command=submitPicture,style="secondary.TButton")
#btnPicture.grid(row=2,column=0,padx=5,pady=2,sticky=tk.W)
#btnQrCode=ttk.Button(master=frame,text='Qr Code',width=8,command=submitQrcode,style="secondary.TButton")
#btnQrCode.grid(row=3,column=0,padx=5,pady=2,sticky=tk.W)
#btnBarCode=ttk.Button(master=frame,text='Bar Code',width=8,command=submitBarcode,style="secondary.TButton")
#btnBarCode.grid(row=4,column=0,padx=5,pady=2,sticky=tk.W)
#canvas=tk.Canvas(master=frame,width=640,height=400,borderwidth=1,background="#fafafa",relief="solid")
#canvas.grid(row=1,column=1,rowspan=12,columnspan=2,padx=5,pady=5,sticky=tk.SE)

#frameService
radio_var=tk.IntVar()
lb_option=ttk.Label(master=frameSevice,text="Options",
                        padding=5,
                      font=('Helvitica',10,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
lb_option.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
rdb_text=ttk.Radiobutton(master=frameSevice,text="Text",variable=radio_var,value=0,command=show_frame)
rdb_text.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
rdb_picture=ttk.Radiobutton(master=frameSevice,text="Picture",variable=radio_var,value=1,command=show_frame)
rdb_picture.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)
rdb_qrcode=ttk.Radiobutton(master=frameSevice,text="Qrcode",variable=radio_var,value=2,command=show_frame)
rdb_qrcode.grid(row=1,column=2,padx=5,pady=5,sticky=tk.W)
rdb_barcode=ttk.Radiobutton(master=frameSevice,text="Barcode",variable=radio_var,value=3,command=show_frame)
rdb_barcode.grid(row=1,column=3,padx=5,pady=5,sticky=tk.W)
frame_text=ttk.Frame(master=frameSevice)
frame_picture=ttk.Frame(master=frameSevice)
frame_qrcode=ttk.Frame(master=frameSevice)
frame_barcode=ttk.Frame(master=frameSevice)
frames=[frame_text,frame_picture,frame_qrcode,frame_barcode]

#frameServiveText
labelTitle =ttk.Label(master=frame_text,text="Propreties",
                      padding=5,
                      font=('Helvitica',10,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelNameText=ttk.Label(master=frame_text,text="Name Fields",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelNameText.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
entry_name_text=ttk.Entry(master=frame_text,width=10)
entry_name_text.grid(row=1,column=1,columnspan=3,sticky=tk.EW,padx=10,pady=10)
labelX=ttk.Label(master=frame_text,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)
textX=tk.StringVar()
textX.set('0')
entry_x_text=ttk.Entry(master=frame_text,width=10,textvariable=textX)
entry_x_text.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frame_text,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)
textY=tk.StringVar()
textY.set('0')
entry_y_text=ttk.Entry(master=frame_text,width=10,textvariable=textY)
entry_y_text.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)
textW=tk.StringVar()
textW.set('0')
labelWidth=ttk.Label(master=frame_text,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entry_width_text=ttk.Entry(master=frame_text,width=10,textvariable=textW)
entry_width_text.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frame_text,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)
textH=tk.StringVar()
textH.set('0')
entry_height_text=ttk.Entry(master=frame_text,width=10,textvariable=textH)
entry_height_text.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)

labelText=ttk.Label(master=frame_text,text="Text",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelText.grid(row=4,column=0,padx=5,pady=5,sticky=tk.EW)
textT=tk.StringVar()
textT.set('Text review')
entry_data_text=ttk.Entry(master=frame_text,width=20,textvariable=textT)
entry_data_text.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

labelFont=ttk.Label(master=frame_text,text="Font Family",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelFont.grid(row=5,column=0,padx=5,pady=5,sticky=tk.EW)

cbFont=ttk.Combobox(master=frame_text,width=15,state="readonly")
cbFont.grid(row=5,column=1,padx=5,pady=5,sticky=tk.W)
cbFont['value']=("Arial","Helvetica","Time New Roman")
cbFont.set("Arial")
cbFont.bind("<<ComboboxSelected>>",changeFont)

labelSize=ttk.Label(master=frame_text,text="Size",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=5,column=2,padx=5,pady=5,sticky=tk.EW)

cbSize=ttk.Combobox(master=frame_text,width=10)
cbSize.grid(row=5,column=3,padx=5,pady=5,sticky=tk.E)
cbSize['value']=("10","12","14","16","18","20","22","24","28","30","32","34","36","38","40","42","46","50","54","58","60","64","68","72","80","90","100")
cbSize.set("20")
cbSize.bind("<<ComboboxSelected>>",changeFont)
labelAlign=ttk.Label(master=frame_text,text="Align",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=6,column=0,padx=5,pady=5,sticky=tk.EW)
btnAlignLeft =ttk.Button(master=frame_text,image=photoLeft,style="secondary.outline.TButton",command=lambda: align_t("left"))
btnAlignLeft.grid(row=6,column=1,padx=5,pady=5,sticky=tk.W)
btnAlignRight =ttk.Button(master=frame_text,image=photoRight,style="secondary.outline.TButton",command=lambda: align_t("right"))
btnAlignRight.grid(row=6,column=1,padx=5,pady=5,sticky=tk.E)
btnAlignCenter =ttk.Button(master=frame_text,image=photoCenter,style="secondary.outline.TButton",command=lambda: align_t("center"))
btnAlignCenter.grid(row=6,column=1,padx=5,pady=5)


#btnAligJustify =ttk.Button(master=frameSevice,image=photo123,style="secondary.outline.TButton")
#btnAligJustify.grid(row=6,column=0,columnspan=2,padx=5,pady=5,sticky=tk.N)
b_var=tk.BooleanVar(master=frame_text)
i_var=tk.BooleanVar(master=frame_text)
u_var=tk.BooleanVar(master=frame_text) 
btnAlignB =ttk.Checkbutton(master=frame_text,image=photoB,variable=b_var,command=align_update)
btnAlignB.grid(row=6,column=2,columnspan=2,padx=15,pady=5,sticky=tk.W)
btnAlignI =ttk.Checkbutton(master=frame_text,image=photoI,variable=i_var,command=align_update)
btnAlignI.grid(row=6,column=2,columnspan=2,padx=15,pady=5,sticky=tk.E)
btnAlignU =ttk.Checkbutton(master=frame_text,image=photoU,variable=u_var,command=align_update)
btnAlignU.grid(row=6,column=2,columnspan=2,padx=5,pady=5)

labelAlign=ttk.Label(master=frame_text,text="Font Color",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=7,column=2,columnspan=2,padx=5,pady=5,sticky=tk.W)


btnFontcolor =ttk.Button(master=frame_text,image=photofgFont,style="secondary.outline.TButton",command=fontcolor)
btnFontcolor.grid(row=7,column=2,columnspan=2,padx=25,pady=5,sticky=tk.E)
color_var_t=tk.StringVar(master=frameSevice)
color_var_t.set("#000000")

labelAlign=ttk.Label(master=frame_text,text="Background Color",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=7,column=0,columnspan=2,padx=5,pady=5,sticky=tk.W)

color_var=tk.StringVar(master=frame_text)
btnBgColor =ttk.Button(master=frame_text,image=photobgFont,style="secondary.outline.TButton",command=backgroundcolor)
btnBgColor.grid(row=7,column=0,columnspan=2,padx=25,pady=5,sticky=tk.E)
color_var.set("#ffffff")

#button service
btnAddText=ttk.Button(master=frame_text,text="Add",style=("secondary.TButton"),width=6,command=add_text)
btnAddText.grid(row=8,column=0,padx=5,pady=10,sticky=tk.E)

btnEditText=ttk.Button(master=frame_text,text="Edit",style=("secondary.TButton"),width=6,command=update_text)
btnEditText.grid(row=8,column=1,padx=15,pady=10)

btnDeleteText=ttk.Button(master=frame_text,text="Delete",style=("secondary.TButton"),width=6,command=delete_text)
btnDeleteText.grid(row=8,column=2,padx=5,pady=10,sticky=tk.W)

btnSeachText=ttk.Button(master=frame_text,text="Seach",style=("secondary.TButton"),width=6,command=seach_text)
btnSeachText.grid(row=8,column=3,padx=5,pady=10,sticky=tk.E)
#frameQrcode
labelTitle =ttk.Label(master=frame_qrcode,text="PROPERTIES",
                      padding=5,
                      font=('Helvitica',12,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelSettingbase=ttk.Label(master=frame_qrcode,text="SETTING BASE",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelSettingbase.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelX=ttk.Label(master=frame_qrcode,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)

entry_x_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_x_qr.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frame_qrcode,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)

entry_y_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_y_qr.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)

labelWidth=ttk.Label(master=frame_qrcode,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entry_width_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_width_qr.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frame_qrcode,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)

entry_height_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_height_qr.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelLink=ttk.Label(master=frame_qrcode,text="Link",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelLink.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

entry_data_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_data_qr.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
entry_data_qr.bind("<Key>",on_entry_key_press)
lbName = ttk.Label(master=frame_qrcode,text="Name",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
lbName.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

entry_name_qr=ttk.Entry(master=frame_qrcode,width=10)
entry_name_qr.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

btncolorQR=ttk.Button(master=frame_qrcode,text="Choese ",command=seach_qr,style="secondary.TButton")
btncolorQR.grid(row=6,column=0,padx=5,pady=5)

btnbgcolorQR=ttk.Button(master=frame_qrcode,text="Save",command=save_qr,style="secondary.TButton")
btnbgcolorQR.grid(row=6,column=1,padx=5,pady=5)
generate_button = ttk.Button(master=frame_qrcode, text="Generate", command=generate_qr_code,style="secondary.TButton")
generate_button.grid(row=6,column=2,padx=5,pady=5)

clear_button = ttk.Button(master=frame_qrcode, text="Clear ", command=clear_qr_code,style="secondary.TButton")
clear_button.grid(row=6,column=3,padx=5,pady=5 )

lbSeach = ttk.Label(master=frame_qrcode,text="Seach",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
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

cbb_seach=ttk.Combobox(master=frame_qrcode,values=name_qr)
cbb_seach.grid(row=7,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

cbb_seach.bind("<<ComboboxSelected>>",seach_qr)
#framePicture
labelTitle =ttk.Label(master=frame_picture,text="PROPERTIES",
                      padding=5,
                      font=('Helvitica',12,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelSettingbase=ttk.Label(master=frame_picture,text="SETTING BASE",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelSettingbase.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelX=ttk.Label(master=frame_picture,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)
textX=tk.StringVar()
textX.set('0')
entry_x_img=ttk.Entry(master=frame_picture,width=10,textvariable=textX)
entry_x_img.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frame_picture,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)
textY=tk.StringVar()
textY.set('0')
entry_y_img=ttk.Entry(master=frame_picture,width=10,textvariable=textY)
entry_y_img.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)
textW=tk.StringVar()
textW.set('0')
lbWidth=ttk.Label(master=frame_picture,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
lbWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entry_width_img=ttk.Entry(master=frame_picture,width=10,textvariable=textW)
entry_width_img.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frame_picture,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)
textH=tk.StringVar()
textH.set('0')
entry_height_img=ttk.Entry(master=frame_picture,width=10,textvariable=textH)
entry_height_img.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelSize=ttk.Label(master=frame_picture,text="Choose picture",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="041199",
    database="pixeluxApp"
)
cursor = connection.cursor()

# Execute SQL query to fetch image names
cursor.execute("SELECT nameimage FROM images_bg")
image_names = [row[0] for row in cursor.fetchall()]

# Close cursor and connection
cursor.close()
connection.close()

cbChoosePicture=ttk.Combobox(master=frame_picture,width=10,values=image_names)
cbChoosePicture.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

display_button = tk.Button(master=frame_picture, text="Create picture", command=display_image)
display_button.grid(row=5,column=0,padx=5,pady=5,sticky=tk.EW)
def save_image():
    x=int(textX.get())
    y=int(textY.get())
    w=int(textW.get())
    h=int(textH.get())
    img_name=cbChoosePicture.get()
    img_path=f"images/bg/{img_name}"
    img = cv2.imread(img_path)
    cropped_img = img[y:y+h, x:x+w]
    cv2.imwrite(f"images/cropped/{img_name}", cropped_img)
    messagebox.showinfo("Success", "Image cropped and saved successfull")
save_button = tk.Button(master=frame_picture, text="Save Image", command=save_image)
save_button.grid(row=5,column=1,padx=5,pady=5,sticky=tk.W)
#frameBarcode
labelTitle =ttk.Label(master=frame_barcode,text="PROPERTIES",
                      padding=5,
                      font=('Helvitica',12,'bold'),
                      background='#f4f4f4',
                      width=max,
                      image=photoService,
                      compound="left")
labelTitle.grid(row=0,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelSettingbase=ttk.Label(master=frame_barcode,text="SETTING BASE",
                           padding=5,
                           font=('Helvitica',10,"bold"),
                           background='#f4f4f4',
                           width=max)
labelSettingbase.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky=tk.NW)

labelX=ttk.Label(master=frame_barcode,text="X",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelX.grid(row=2,column=0,padx=5,pady=5,sticky=tk.NW)
textX=tk.StringVar()
textX.set('0')
entry_x_barcode=ttk.Entry(master=frame_barcode,width=10,textvariable=textX)
entry_x_barcode.grid(row=2,column=1,padx=5,pady=5,sticky=tk.NW)

labelY=ttk.Label(master=frame_barcode,text="Y",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelY.grid(row=2,column=2,padx=5,pady=5,sticky=tk.NW)
textY=tk.StringVar()
textY.set('0')
entry_y_barcode=ttk.Entry(master=frame_barcode,width=10,textvariable=textY)
entry_y_barcode.grid(row=2,column=3,padx=5,pady=5,sticky=tk.NW)
textW=tk.StringVar()
textW.set('0')
labelWidth=ttk.Label(master=frame_barcode,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidth.grid(row=3,column=0,padx=5,pady=5,sticky=tk.NW)

entryWidth=ttk.Entry(master=frame_barcode,width=10,textvariable=textW)
entryWidth.grid(row=3,column=1,padx=5,pady=5,sticky=tk.NW)

labelHeight=ttk.Label(master=frame_barcode,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeight.grid(row=3,column=2,padx=5,pady=5,sticky=tk.NW)
textH=tk.StringVar()
textH.set('0')
entryHeight=ttk.Entry(master=frame_barcode,width=10,textvariable=textH)
entryHeight.grid(row=3,column=3,padx=5,pady=5,sticky=tk.NW)



labelSize=ttk.Label(master=frame_barcode,text="Link",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelSize.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)

entryLinkBarcode=ttk.Entry(master=frame_barcode,width=10)
entryLinkBarcode.grid(row=4,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)

generate_button = tk.Button(master=frame_barcode, text="Generate Barcode", command=generate_barcode)
generate_button.grid(row=5,column=0,columnspan=2)

clear_button = tk.Button(master=frame_barcode, text="Clear Barcode", command=clear_barcode)
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

cbSizeTable=ttk.Combobox(master=frameInterface,
                        state="readonly")

cbSizeTable.grid(row=2,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
size_names=get_size_names()

cbSizeTable['values']=size_names


labelWidthT=ttk.Label(master=frameInterface,text="Width",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelWidthT.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)

entry_size_width=ttk.Entry(master=frameInterface,width=10)
entry_size_width.grid(row=3,column=0,padx=5,pady=5,sticky=tk.E)

labelHeightT=ttk.Label(master=frameInterface,text="Height",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelHeightT.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)

entry_size_height=ttk.Entry(master=frameInterface,width=10)
entry_size_height.grid(row=3,column=1,padx=5,pady=5,sticky=tk.E)
cbSizeTable.bind("<<ComboboxSelected>>",show_size)
btnAlignU =ttk.Button(master=frameInterface,text="Update",image=photoUpload,compound="left",style="secondary.outline.TButton",command=updateSizeTemplate)
btnAlignU.grid(row=3,column=2,padx=25,pady=5,sticky=tk.E)

labelAlign=ttk.Label(master=frameInterface,text="Add BackGround",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=4,column=2,columnspan=2,padx=5,pady=5,sticky=tk.W)

btnAlignU =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=add_image)
btnAlignU.grid(row=4,column=2,columnspan=2,padx=25,pady=5,sticky=tk.E)

labelAlign=ttk.Label(master=frameInterface,text="Add Picture",padding=5,font=('Helvitica',8,"bold"),background='#f4f4f4',width=max)
labelAlign.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky=tk.W)

btnAlignU =ttk.Button(master=frameInterface,text="Import File",image=photoPicture,compound="left",style="secondary.outline.TButton",command=add_image)
btnAlignU.grid(row=4,column=0,columnspan=2,padx=25,pady=5,sticky=tk.E)

lebleChooseBackground=ttk.Label(master=frameInterface,text="Chose Background",
                            font=('Helvitica',8,"bold"),
                            background='#f4f4f4',
                            
                            )
lebleChooseBackground.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)

cbBackGround=ttk.Combobox(master=frameInterface,values=image_names)
cbBackGround.grid(row=5,column=1,columnspan=3,padx=5,pady=5,sticky=tk.EW)
#frameCode
frameCode =ttk.Frame(master=root,border=1,relief=SUNKEN)
frameCode.grid(row=1,column=2,padx=10,pady=10,sticky=tk.NW)

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
#scrollbar.grid(row=0,column=2,rowspan=2,sticky=tk.NS)





root.mainloop()