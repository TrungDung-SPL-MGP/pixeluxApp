



def new():
    print ("New File")
    
def open():
    file_name=tk.askopenfilename(initialdir="/", title="Select file" ,filetypes=(("text files","*.txt"),("all files","*.*")))
    file_name = fd.askopenfilename(parent=root,
                                filetypes=[("All Files", "*.*"), ("Text files", "*.txt")])
    if file_name:
        print ("Opening file", file_name)
        
def saveas():
    file_name = fd.asksaveasfilename(initialdir="c:/", initialfile="untitled.txt",
                                  title="Select file to save as",
                                  filetypes=(("Text files","*.txt"),("all files","*.*")))
    print ("Saving file ", file_name)
    
def exit_program():
    root.quit()   # stop the main loop
    root.destroy 
def langguage():
    """Show text in status bar."""
    showStatusBarVar.set(showStatusBarVar.get())
def insert(event):
    try:
        text.insert('insert', event.widget.get('selection'))
    except tk.TclError:
        pass
def tableCard():
    print("table card info")
          


def click(event):
    print('g')

def managerSystem():
    print('d')
def contact():
   messagebox.showinfo(title="Contact", message="Email: spacelight@contact.vn")
def about():
   messagebox.showinfo(title="Infomation App",message="SpaceLight Co Company Stress:171 Dao Duy Anh,waPhu Nhuan,HoChiMinh city")
def change_color():
    colors =colorchooser.askcolor(title="Chooser Color")
    root.configure(bg=colors[1])
def switch(lb,page):   
    for child in options_p.winfo_children():
        if isinstance(child,ttk.Label):
            print("123")
        
    print("hello")
    for fm in main_p.winfo_children():
        fm.destroy()
        root.update()
    page()
def home_page():
    home_page_p=ttk.Frame(master=main_p,border=2,borderwidth=1,relief="solid")
    
    lbHome =ttk.Label(master=home_page_p,text="Home 1 page",font=("Helvitica",14))
    lbHome.grid(row=0,column=0)
    btnSave=ttk.Button(master=home_page_p,text='Save Temp',width=10,image=photoSave,compound="left",style="secondary.TButton")
    btnSave.grid(row=0,column=2,padx=5,pady=5,sticky=tk.E)
    btnPreview=ttk.Button(master=home_page_p,text='Preview',width=10,compound='left',style="secondary.TButton")
    btnPreview.grid(row=0,column=2,padx=5,pady=5)


    service_frame=ttk.Frame(master=home_page_p,border=2,borderwidth=1,relief="solid")
    service_frame.grid(row=0,column=3,columnspan=2,padx=5,pady=5,sticky=tk.SE)
    option_service=ttk.Frame(master=service_frame)
    option_service.pack(pady=5,padx=5)
    option_service.pack_propagate(False)
    option_service.configure(width=500,height=35)
    def show_frame(frame):
        frame.tkraise()
    def select_on():
        selected_frame=combobox_fields.get()
        if selected_frame=="Text":
            show_frame(fields_text)
        elif selected_frame=="Picture":
            show_frame(fields_picture)
        elif selected_frame=="Qr Code":
            show_frame(fields_qrcode)
        elif selected_frame=="Bar Code":
            show_frame(fields_barcode)    
    fields_text=ttk.Frame(master=service_frame) 
    fields_picture=ttk.Frame(master=service_frame) 
    fields_qrcode=ttk.Frame(master=service_frame) 
    fields_barcode=ttk.Frame(master=service_frame)

    #fields_text.grid(row=1,column=1,sticky=tk.NSEW)
    #fields_picture.grid(row=1,column=1,sticky=tk.NSEW)
    #fields_qrcode.grid(row=1,column=1,sticky=tk.NSEW)
    #fields_barcode.grid(row=1,column=1,sticky=tk.NSEW)    
    for frame in(fields_text,fields_picture,fields_qrcode,fields_barcode):
        frame.place(relwidth=1,relheight=1)
    show_frame(fields_text)

    frame_selection=ttk.Frame(master=home_page_p)
    frame_selection.grid(row=0,column=0,padx=10,pady=10)
    frames=['Text','Picture','Qr Code','Bar Code']
    combobox_fields=ttk.Combobox(frame_selection,values=frames)
    combobox_fields.grid(row=0,column=1)
    combobox_fields.set(frames[0])

    combobox_fields.bind("<<ComboboxSelected>>",select_on)

    home_page_p.grid_rowconfigure(0,weight=1)
    home_page_p.grid_columnconfigure(0,weight=1)

    #menu_bar=tk.Menu(master=home_page_p)
    #home_page_p.config(menu=menu_bar)
    #file_menu_p=tk.Menu(master=menu_bar,tearoff=0)
    #menu_bar.add_cascade(label="Option",menu=file_menu_p)
    #file_menu_p.add_command(label="Text",command=lambda:show_frame(fields_text))
    #file_menu_p.add_command(label="Text",command=lambda:show_frame(fields_picture))
    #file_menu_p.add_command(label="Text",command=lambda:show_frame(fields_qrcode))
    #file_menu_p.add_command(label="Text",command=lambda:show_frame(fields_barcode))
    #btnText=ttk.Button(master=option_service,text='Text',width=8,command=lambda:(print("hello")),style="secondary.TButton")
    #btnText.grid(row=0,column=0,padx=5,pady=2,sticky=tk.W)
    #btnPicture=ttk.Button(master=option_service,text='Picture',width=8,command=lambda:(print("hello")),style="secondary.TButton")
    #btnPicture.grid(row=0,column=1,padx=5,pady=2,sticky=tk.W)
    #btnQrCode=ttk.Button(master=option_service,text='Qr Code',width=8,command=lambda:(print("hello")),style="secondary.TButton")
    #btnQrCode.grid(row=0,column=2,padx=5,pady=2,sticky=tk.W)
    #btnBarCode=ttk.Button(master=option_service,text='Bar Code',width=8,command=lambda:(print("hello")),style="secondary.TButton")
    #btnBarCode.grid(row=0,column=3,padx=5,pady=2,sticky=tk.W)
    canvas=tk.Canvas(master=home_page_p,width=640,height=400,borderwidth=1,background="#fafafa",relief="solid")
    canvas.grid(row=1,column=1,rowspan=12,columnspan=2,padx=5,pady=5,sticky=tk.SE)
   
     
    home_page_p.pack(fill=tk.BOTH, expand=True)
def room_page():
    room_page_p=ttk.Frame(master=main_p,border=2)
    
    lbRoom =ttk.Label(master=room_page_p,text="Home 2page",font=("Helvitica",14))
    lbRoom.pack(pady=10)
    room_page_p.pack(fill=tk.BOTH, expand=True)
def temp_page():
    temp_page_p=ttk.Frame(master=main_p,border=2)
    
    lbTem =ttk.Label(master=temp_page_p,text="Home 3page",font=("Helvitica",14))
    lbTem.pack(pady=10)
    temp_page_p.pack(fill=tk.BOTH, expand=True)
def about_page():
    about_page_p=ttk.Frame(master=main_p,border=2)
    
    lbAbout =ttk.Label(master=about_page_p,text="Home 4page",font=("Helvitica",14))
    lbAbout.pack(pady=10)
    about_page_p.pack(fill=tk.BOTH, expand=True) 


      
import tkinter as tk
from tkinter import Menu, PhotoImage,messagebox,colorchooser
import ttkbootstrap as ttk
from tkinter import filedialog as fd
from tkinter.filedialog import Open,SaveAs,SaveFileDialog,askopenfilenames,askopenfilename
import os, sys
root =ttk.Window(themename='superhero')
root.title('Pixelux App v1.0')

root.geometry("1200x680")

#photo 
#def __init__(self):
    #self.photo = PhotoImage(file="assets/images/save.png")
    #self.root.iconphoto(False, self.photo)

    

photoSave = PhotoImage(file="assets/images/save/Web/1.png")
photoOpen = PhotoImage(file="assets/images/foder/Web/1.png")
photoNew = PhotoImage(file="assets/images/open/Web/1.png")
photoEdit = PhotoImage(file="assets/images/output/Web/1.png")
photoLanguage= PhotoImage(file="assets/images/langcolor/Web/1.png")
photoLanguageVN= PhotoImage(file="assets/images/vietnam/Web/1.png")
photoLanguageEN= PhotoImage(file="assets/images/english/Web/1.png")
photoContact= PhotoImage(file="assets/images/phone/Web/1.png")
photoAbout= PhotoImage(file="assets/images/about/Web/1.png") 
photoTable= PhotoImage(file="assets/images/card/Web/1.png")
photoDevice= PhotoImage(file="assets/images/processor/Web/1.png")   
photoColor=PhotoImage(file="assets/images/langcolor/Web/1.png") 
#File
menubar=Menu(root)
file_menu=Menu(menubar,tearoff=False)

menubar.add_cascade(label="File", menu=file_menu)

#footer
showStatusBarVar=tk.StringVar()
showStatusBarVar.set("@2014-2024 SpaceLight.All rights reserved.")
statusbar=tk.Label(root, textvariable=showStatusBarVar)
statusbar.pack(side="bottom" , fill="x")

#edit
edit_menu=Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edit", menu=edit_menu)
subMenu =Menu(edit_menu,takefocus=0)
subMenu.add_command(label="Vietnamese",image=photoLanguageVN,compound="left")
subMenu.add_command(label="EngLish",image=photoLanguageEN,compound="left")

edit_menu.add_cascade(
    label="Language",
    menu=subMenu
    ,image=photoLanguage,compound="left"
)
edit_menu.add_command(label='Choose Background Color',image=photoColor,compound='left',command=change_color)
#device
device_menu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='Device',menu=device_menu)
device_menu.add_command(label="Manage System",image=photoDevice,compound="left",command=managerSystem)
device_menu.add_command(label="Table card",image=photoTable,compound="left",command=tableCard)
#Help
help_menu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label="About",image=photoAbout,compound="left",command=about)
help_menu.add_command(label="Support Contact",image=photoContact,compound="left",command=contact)
#view

# Display menubar on root window
root.config(menu=menubar)

options_p=tk.Frame(root,bg="gray",borderwidth=1,relief="solid")

btnHome =ttk.Button(options_p,text="Home",style=("info.Outline.TButton"),command=lambda: switch(lb=lbHome,page=home_page))
btnHome.place(x=5,y=0,width=125)

lbHome=ttk.Label(master=options_p)
lbHome.place(x=30.,y=28,width=69,height=2)

btnRoom =ttk.Button(options_p,text="Room",style=("info.Outline.TButton"),command=lambda: switch(lb=lbRoom,page=room_page))
btnRoom.place(x=125,y=0,width=125)

lbRoom=ttk.Label(master=options_p)
lbRoom.place(x=155.,y=28,width=69,height=2)

btnTemHome =ttk.Button(options_p,text="Template",style=("info.Outline.TButton"),command=lambda: switch(lb=lbTemHome,page=temp_page))
btnTemHome.place(x=250,y=0,width=125)

lbTemHome=ttk.Label(master=options_p)
lbTemHome.place(x=280.,y=28,width=69,height=2)

btnAboutH =ttk.Button(options_p,text="About",style=("info.Outline.TButton"),command=lambda: switch(lb=lbAboutH,page=about_page))
btnAboutH.place(x=375,y=0,width=125)

lbAboutH=ttk.Label(master=options_p)
lbAboutH.place(x=405.,y=28,width=69,height=2)

options_p.pack(pady=5,padx=5)
options_p.pack_propagate(False)
options_p.configure(width=500,height=35)
main_p=tk.Frame(root,bg="gray",borderwidth=5,relief="solid")


main_p.pack(fill=tk.BOTH,expand=True)

home_page()


text=tk.Text(root)
scrollbar=tk.Scrollbar(root)
#scrollbar.pack(side="right",fill="y")

#text.pack(side="left", fill="both", expand=True)
#scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

text.bind("<Control-v>", insert)
 
root.mainloop()