class Colors:
    empty=(45,59,67)
    red = (239,4,4)
    orange=(239,151,4)
    yellow = (239,191,4)
    green = (4,239,54)
    blue = (69,15,239)
    indigo=(4,216,239)
    violet = (160,61,255)
    line_color=(16,17,30)
    text_color= (255, 255, 255)
    light_grey=(58,58,65)

    @classmethod
    def block_colors(cls):
        return [cls.empty, cls.red, cls.orange, cls.yellow, cls.green, cls.blue, cls.indigo,cls.violet]