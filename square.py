

WHITE = (255,255,255)

class Square:
    def __init__(self, start=None, velocity=None, size=None, color=None):
        if start is None:
            start = [0,0]
        self.pos = list(start)

        if velocity is None:
            velocity = [0,0]
        self.velocity = velocity

        if size is None:
            size = 10
        self.size = size

        if color is None:
            color = WHITE
        self.color = color


    def update_position(self, maze_map):
        new_x = self.pos[0] + self.velocity[0]
        new_y = self.pos[1] + self.velocity[1]
        if all( not maze_map.get(corner) for corner in get_corners(new_x,new_y,self.size)):
            self.pos[0] = new_x
            self.pos[1] = new_y
        else:
            print 'collision'

def get_corners(x,y,size):
    corners = [(x,y),(x+size,y),(x,y+size),(x+size,y+size)] 
    return corners   

