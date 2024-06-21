class PictureField:
    def __init__(self,id,x,y,width,height, name, value,brightness,transparency,active):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.brightness = brightness
        self.transparency = transparency
        self.active = active
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
    def set_value(self,value):#value is a string
        self.value=value
    def get_value(self):
        return self.value
    def set_brightness(self,brightness):
        self.brightness=brightness
    def get_brightness(self):
        return self.brightness
    def set_transparency(self,transparency):
        self.transparency=transparency
    def get_transparency(self):
        return self.transparency
    def set_active(self,active):
        self.active=active
    def get_active(self):
        return self.active