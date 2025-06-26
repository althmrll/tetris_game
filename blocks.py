from general_block_characteristic import GeneralBlock
from block_position import BlockPosition

class IBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=1)
        self.cells={
            0: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(1,3)],
            1: [BlockPosition(0,2),BlockPosition(1,2),BlockPosition(2,2), BlockPosition(3,2)],
            2: [BlockPosition(2,0),BlockPosition(2,1),BlockPosition(2,2), BlockPosition(2,3)],
            3: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(3,1)]
        }
        self.move(-1,3)

class TBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0: [BlockPosition(0,1),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,1)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,1)],
            3: [BlockPosition(0,1),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(2,1)]
        }
        self.move(0,3)

class JBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=3)
        self.cells={
            0: [BlockPosition(0,0),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(0,2),BlockPosition(1,1), BlockPosition(2,1)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,2)],
            3: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,0), BlockPosition(2,1)]
        }
        self.move(0,3)

class ZBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=4)
        self.cells={
            0: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,2),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,1)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            3: [BlockPosition(0,1),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(2,0)]
        }
        self.move(0,3)

class LBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=5)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }
        self.move(0,3)

class OBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=6)
        self.cells={
            0: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            1: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            2: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,0), BlockPosition(1,1)]
        }
        self.move(0,4)

class SBlock(GeneralBlock):
    def __init__(self):
        super().__init__(id=7)
        self.cells={
            0: [BlockPosition(0,1),BlockPosition(0,2),BlockPosition(1,0), BlockPosition(1,1)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,2)],
            2: [BlockPosition(1,1),BlockPosition(1,2),BlockPosition(2,0), BlockPosition(2,1)],
            3: [BlockPosition(0,0),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(2,1)]
        }
        self.move(0,3)