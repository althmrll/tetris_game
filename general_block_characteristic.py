from color_scheme import Colors

class GeneralBlock:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cell_size=30
        self.rotation_state=0
        self.colors=Colors.block_colors()
    
    def draw(self, screen):
        ...