
class Army():
    
    def __init__(self, owner, size, coordinates):

        self.size = size
        self.owner = owner
        self.coordinates = coordinates

    def get_owner(self):
        return self.owner
    
    def get_size(self):
        return self.size
    
    def get_coordinates(self):
        return self.coordinates