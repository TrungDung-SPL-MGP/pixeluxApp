class TextField:
    def __init__(self, id,text, x, y, width, height, font,font_size,font_color,font_bg,align,align_font,active):
        self.id = id
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.font_bg = font_bg
        self.active = active
        self.align=align
        self.align_font=align_font
        
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
    def set_color(self,font_color):
        self.color=font_color
    def get_color(self):
        return self.font_color
    def set_text(self,text):
        self.text=text
    def get_text(self):
        return self.text
    def set_font(self,font):
        self.font=font
    def get_font(self):
        return self.font
    def set_font_size(self,font_size):
        self.font_size=font_size
    def get_font_size(self):
        return self.font_size
    def set_font_bg(self,font_bg):
        self.font_bg=font_bg
    def get_font_bg(self):
        return self.font_bg
    def set_active(self,active):
        self.active=active
    def get_active(self):
        return self.active
    def set_align(self,align):
        self.align=align
    def get_align(self):
        return self.align
    def set_align_font(self,align_font):
        self.align_font=align_font
    def get_align_font(self):
        return self.align_font    

        