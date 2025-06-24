from general_block_characteristic import GeneralBlock
from block_position import BlockPosition

class OBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=1)
        self.cells={
            0: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            1: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            2: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=3)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=4)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=5)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=6)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=7)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }