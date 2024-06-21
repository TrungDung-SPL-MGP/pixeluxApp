import tkinter as tk
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk

def generate_barcode():
    data = data_entry.get()

    # create barcode
    barcode_class = barcode.get_barcode_class('code128')  # 'code128'
    barcode_instance = barcode_class(data, writer=ImageWriter())
    barcode_img = barcode_instance.render()

    
    barcode_img = ImageTk.PhotoImage(barcode_img)

    # Hiển thị mã vạch trên Canvas
    barcode_canvas.create_image(0, 0, anchor=tk.NW, image=barcode_img)
    barcode_canvas.image = barcode_img

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Barcode Generator")

# Tạo trường nhập dữ liệu cho mã vạch
data_label = tk.Label(root, text="Enter data:")
data_label.pack()
data_entry = tk.Entry(root, width=40)
data_entry.pack()

# Tạo nút để tạo mã vạch
generate_button = tk.Button(root, text="Generate Barcode", command=generate_barcode)
generate_button.pack()

# Tạo Canvas để hiển thị mã vạch
barcode_canvas = tk.Canvas(root, width=600, height=100)
barcode_canvas.pack()

root.mainloop()
