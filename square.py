

WHITE = (255,255,255)

class Square:
    def __init__(self, start=None, velocity=None, size=None, color=None):
        if start is None:
            start = [0,0]
        self.pos = start

        if velocity is None:
            velocity = [0,0]
        self.velocity = velocity

        if size is None:
            size = 10
        self.size = size

        if color is None:
            color = WHITE
        self.color = color


    def update_position(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
