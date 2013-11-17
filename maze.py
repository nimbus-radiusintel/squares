#!/usr/bin/env python
import sys
from random import shuffle
from square import Square

def shuffled(x):
    y = list(x)
    shuffle(y)
    return y

DIRECTIONS = (
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
)


def get_maze_squares():
    maze = make_maze(5,5,1)
    print maze
    print len(maze)
    chunk_size = 11
    rows = []
    for i in range(chunk_size):  
        row = maze[chunk_size*(i):chunk_size*(i+1)]
        rows.append(row)
    print rows
    mazeblocks = []
    for i in range(chunk_size):
        curr_row = rows[i]
        for j in range(chunk_size):
            if curr_row[j] == 1:
                x = (float(j)/chunk_size)*320
                y = (float(i)/chunk_size)*240
                maze_square = Square(start = (x,y), color = (40, 200, 40))
                print (x,y)
                mazeblocks.append(maze_square)
    return mazeblocks


def make_maze(width, height, cellsize):
    cellsize1 = cellsize+1 # cellsize including one wall
    field_width = width*cellsize1+1
    field_height = height*cellsize1+1
    field = [0]*(field_width*field_height)
    stack = [(0, 0, shuffled(DIRECTIONS))]
    while stack:
        x, y, directions = stack[-1]
        dx, dy = directions.pop()
        # no other ways to go from here
        if not directions:
            stack.pop()
        # new cell
        nx = x+dx
        ny = y+dy
        # out of bounds
        if not (0 <= nx < width and 0 <= ny < height):
            continue
        # index of new cell in field
        fx = 1+nx*cellsize1
        fy = 1+ny*cellsize1
        fi = fx+fy*field_width
        # already visited
        if field[fi]:
            continue
        # tear down walls
        if dx > 0:
            a = -1
            b = field_width
        elif dx < 0:
            a = cellsize
            b = field_width
        elif dy > 0:
            a = -field_width
            b = 1
        else:
            a = cellsize*field_width
            b = 1
        for offset in xrange(cellsize):
            field[fi+a+b*offset] = 1
        # clear cell
        for y in xrange(0, cellsize):
            for x in xrange(0, cellsize):
                field[fi+x+y*field_width] = 1
        # visit cell
        stack.append([nx, ny, shuffled(DIRECTIONS)])
    return field

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("Usage: %s width height cellsize" % sys.argv[0])
    width, height, cellsize = map(int, sys.argv[1:])
    fields = make_maze(width, height, cellsize)
    w = (cellsize+1)*width+1
    h = (cellsize+1)*height+1
    for y in xrange(h):
        print "".join(map(lambda x: x and " " or "#", fields[y*w:y*w+w]))