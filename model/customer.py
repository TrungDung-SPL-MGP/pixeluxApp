class Customer:
    def __init__(self, id,name,position,rank,address,gender):
        self.id=id
        self.name=name
        self.posision=position
        self.rank=rank
        self.address=address
        self.gender=gender
    def get_id(self):
        return self.id
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_position(self,position):
        self.posision=position
    def get_position(self):   
        return self.posision
    def set_rank(self,rank):
        self.rank=rank
    def get_rank(self):
        return self.rank        
    def set_address(self,address):
        self.address=address
    def get_address(self):
        return self.address
    def set_gender(self,gender):
        self.gender=gender
    def get_gender(self):
        return self.gender


