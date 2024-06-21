class TableCard:
    def __init__(self,id,name,width,height,active):
        self.id=id
        self.name= name
        self.width= width
        self.height= height
        self.active= active
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_width(self,width):
        self.width=width
    def get_width(self):
        return self.width
    def set_height(self,height):
        self.height=height
    def get_height(self):
        return self.height
    def set_active(self,active):
        self.active=active
    def get_active(self):
        return self.active                    
        