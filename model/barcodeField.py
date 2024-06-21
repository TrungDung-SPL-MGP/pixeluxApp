class BarCodeField:
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