import tkinter as tk
from tkinter import END, Menu, ttk,messagebox,filedialog
import os.path

import os
from tkinter.colorchooser import askcolor
from turtle import fd
def makecenter(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2) 
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class App(tk.Tk):
    def  __init__(self):
   
        super().__init__()

        self.geometry('250x150+1000+400')
        self.title("Login App")
        self.resizable(False, False)

        #ui
        paddings={'padx':5,'pady':5}
        entry_font={'font':('Helvetica',10)}

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        self.username = tk.StringVar()
        self.password=tk.StringVar()
        
        lbl_username = ttk.Label(self,text="Username:")
        lbl_username.grid(row=0,column=0,sticky=tk.W,**paddings)

        etr_username=ttk.Entry(self,textvariable=self.username,**entry_font)
        etr_username.grid(row=0,column=1,sticky=tk.EW,**paddings)

        lbl_password = ttk.Label(self,text="Password:")
        lbl_password.grid(row=1,column=0,sticky=tk.W,**paddings)

        etr_password=ttk.Entry(self,textvariable=self.password,show='*',**entry_font)
        etr_password.grid(row=1,column=1,sticky=tk.EW,**paddings)

        btnLogin =ttk.Button(self,text='Login',command=self.checkLogin)
        btnLogin.grid(row=2,column=0,columnspan=2,sticky=tk.S+tk.E,**paddings)

        self.style =ttk.Style()
        self.style.configure('TLabel',font=(('Helvetica',10)))
        self.style.configure('TButton',font=('Helvetica',10))

    def checkLogin(self):
        if self.username.get()=="admin" and self.password.get()=="123":
            messagebox.showinfo("Success","You are logged in!")
            print('Logged In successfull')
            
            
            
            try:
                root =tk.Tk()
                root.title('Table card management system v1.0')
                root.resizable(height=True,width=True)
                root.minsize(height=350,width=500) 
                #menubar
               

                def new():
                    print ("New File")
                    
                def open():
                    openFile = open(filedialog.askopenfilename())
                    data =openFile.read()
                    loadFile.insert(END,data)
                    openFile.close()
                        
                def save():
                    openFile =open(filedialog.asksaveasfilename(),mode='w')
                    data=openFile.write(loadFile.get(1.0,END))
                    openFile.close()
                def saveas():
                    root.quit()    
                def exit_program():
                    root.quit()   # stop the main loop
                    root.destroy
                menubar =Menu(root)
                root.config(menu=menubar)
                file_menu =Menu(menubar,tearoff=False)
                menubar.add_cascade(label="File", menu=file_menu)
                loadFile= tk.Text(root, height=8, width=40,font=('Helvetica',9),bg='lightgrey').pack(pady=20)
                
                file_menu.add_command(label="New", command=new)
                file_menu.add_command(label="Open", command=open)
                file_menu.add_command(label="Save", command=save)
                file_menu.add_command(label="SaveAs", command=saveas)
                
                file_menu.add_separator()
                file_menu.add_command(label="Exit", command=exit_program)
                #submenu
                def deleteAll():
                    messagebox.showerror("Error", "Are you delete all !!!.")
                    root.quit()
                def choseColor():
                    colors =askcolor(title="Choose a color")
                    root.configure(bg=colors[1])
                    
                edit_menu= Menu(menubar, tearoff= False)
                subMenu =Menu(edit_menu)
                menubar.add_cascade(label="Edit",menu=edit_menu)
                edit_menu.add_cascade(label="Delete",menu=subMenu)
                subMenu.add_command(label="DeleteAll",command=deleteAll)
                subMenu.add_command(label="Color",command=choseColor)
          
                makecenter(root)
                root.mainloop()
                root.quit()
            except:
                print('system  error!') 
                messagebox.CANCEL
               
               

        
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            print('Failed to login')
        

if __name__=='__main__':
    app=App()
    makecenter(app)
    app.mainloop()        

        
        
    