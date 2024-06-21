import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import mysql.connector

def generate_qr_code():
    global qr_img_tk, qr_id
    
    link = link_entry.get()
    x = int(x_entry.get())
    y = int(y_entry.get())
    name = name_entry.get()
    data = data_entry.get()

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
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Resize the QR image to fit the canvas
    qr_img = qr_img.resize((1200, 640), Image.ANTIALIAS)
    
    # Convert QR image to PhotoImage
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    
    # Hiển thị hình ảnh trên Canvas tại vị trí được chỉ định
    qr_id = qr_canvas.create_image(x, y, anchor=tk.NW, image=qr_img_tk)
    
    # Bind mouse events to allow dragging
    qr_canvas.tag_bind(qr_id, "<ButtonPress-1>", start_drag)
    qr_canvas.tag_bind(qr_id, "<B1-Motion>", drag)
    
    # Save QR code data to MySQL database
    save_to_database(x, y, qr_img.width(), qr_img.height(), name, data)

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
    qr_canvas.move(qr_id, dx, dy)
    
    last_x = new_x
    last_y = new_y
    
    # Update x and y entry fields
    x_entry.delete(0, tk.END)
    x_entry.insert(0, str(new_x))
    y_entry.delete(0, tk.END)
    y_entry.insert(0, str(new_y))

def save_to_database(x, y, width, height, name, data):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="041199",
        database="pixeluxApp"
    )
    cursor = conn.cursor()
    
    # SQL query to insert QR code data into the table
    query = "INSERT INTO fields_qr_code (x_qrcode, y_qrcode, width_qrcode, height_qrcode, name, data, active, id_canvas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (x, y, width, height, name, data, 1, 1)  # Adjust 'active' and 'id_canvas' values accordingly
    
    # Execute the SQL query
    cursor.execute(query, values)
    
    # Commit changes to the database
    conn.commit()
    
    # Close database connection
    cursor.close()
    conn.close()

root = tk.Tk()
root.title("QR Code Generator")

# Tạo trường nhập link
link_label = tk.Label(root, text="Enter link:")
link_label.pack()
link_entry = tk.Entry(root, width=40)
link_entry.pack()

# Tạo trường nhập tọa độ x và y
x_label = tk.Label(root, text="Enter X coordinate:")
x_label.pack()
x_entry = tk.Entry(root, width=10)
x_entry.pack()

y_label = tk.Label(root, text="Enter Y coordinate:")
y_label.pack()
y_entry = tk.Entry(root, width=10)
y_entry.pack()

# Tạo trường nhập tên
name_label = tk.Label(root, text="Enter name:")
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Tạo trường nhập dữ liệu
data_label = tk.Label(root, text="Enter data:")
data_label.pack()
data_entry = tk.Entry(root, width=40)
data_entry.pack()

# Tạo nút để tạo mã QR
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Tạo Canvas với kích thước 1200x640
qr_canvas = tk.Canvas(root, width=1200, height=640, bg="white")
qr_canvas.pack()

# Global variables to keep track of last mouse position
last_x = 0
last_y = 0

root.mainloop()
