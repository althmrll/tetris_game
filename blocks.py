from general_block_characteristic import GeneralBlock
from block_position import BlockPosition

class LBlock(GeneralBlock):
    def __init__(self):
        super.__init__(id=1)
        self.cells={
            0: [BlockPosition(0,2),BlockPosition(1,0),BlockPosition(1,1), BlockPosition(1,2)],
            1: [BlockPosition(0,1),BlockPosition(1,1),BlockPosition(2,1), BlockPosition(2,2)],
            2: [BlockPosition(1,0),BlockPosition(1,1),BlockPosition(1,2), BlockPosition(2,0)],
            3: [BlockPosition(0,0),BlockPosition(0,1),BlockPosition(1,1), BlockPosition(2,1)]
        }