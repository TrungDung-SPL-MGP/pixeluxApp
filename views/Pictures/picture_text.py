import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from ttkbootstrap import ttk
def display_image():
    global img_tk, image_label, x_entry, y_entry, width_entry, height_entry
    
    selected_image = image_combobox.get()
    image_path = get_image_path(selected_image)
    
    if image_path:
        # Load image from file
        img = Image.open(image_path)
        
        # Resize image to fit canvas
        img = img.resize((canvas_width, canvas_height))
        
        # Convert image to PhotoImage
        img_tk = ImageTk.PhotoImage(img)
        
        # Display image on canvas
        canvas.create_image(canvas_width/2, canvas_height/2, image=img_tk, tags="image")
        
        # Save a reference to the image to prevent it from being garbage collected
        canvas.image = img_tk
        
        # Update entry fields with initial values
        x_entry.delete(0, tk.END)
        x_entry.insert(0, str(canvas_width/2))
        y_entry.delete(0, tk.END)
        y_entry.insert(0, str(canvas_height/2))
        width_entry.delete(0, tk.END)
        width_entry.insert(0, str(canvas_width))
        height_entry.delete(0, tk.END)
        height_entry.insert(0, str(canvas_height))
        
        # Enable resize button
        resize_button["state"] = tk.NORMAL

def resize_image():
    global img_tk, image_label
    
    # Get new values from entry fields
    x = int(x_entry.get())
    y = int(y_entry.get())
    width = int(width_entry.get())
    height = int(height_entry.get())
    
    # Delete existing image on canvas
    canvas.delete("image")
    
    # Resize image to new dimensions
    img = img_tk._PhotoImage__photo.subsample(width=img_tk.width() // width, height=img_tk.height() // height)
    
    # Display resized image on canvas
    canvas.create_image(x, y, image=img, tags="image")
    
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

root = tk.Tk()
root.title("Image Viewer")

# Connect to MySQL database to fetch image names
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

# Create ComboBox for selecting image
image_combobox = tk.ttk.Combobox(root, values=image_names)
image_combobox.pack()

# Create canvas to display images
canvas_width = 1200
canvas_height = 640
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white",borderwidth=1,relief="solid")
canvas.pack()

# Create entry fields for x, y, width, and height
x_label = tk.Label(root, text="X:")
x_label.pack()
x_entry = tk.Entry(root, width=10)
x_entry.pack()

y_label = tk.Label(root, text="Y:")
y_label.pack()
y_entry = tk.Entry(root, width=10)
y_entry.pack()

width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root, width=10)
width_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root, width=10)
height_entry.pack()

# Create buttons for displaying and resizing image
display_button = tk.Button(root, text="Display Image", command=display_image)
display_button.pack()

resize_button = tk.Button(root, text="Resize Image", command=resize_image, state=tk.DISABLED)
resize_button.pack()

root.mainloop()
