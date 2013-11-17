import pygame
import time
from pygame.locals import *
import random
import math

size = width, height = 320, 240

WHITE = (255,255,255)
BLUE = (50,50,200)
RED = (255, 0, 0)
GREEN = (40, 200, 40)
TILESIZE = 10

def draw_grid(screen, n=None):
    if n is None:
        n = max(width, height) / TILESIZE
    for i in range(n):
        x = i*TILESIZE 
        pygame.draw.line(screen, WHITE, (x, 0), (x, height))
    for i in range(n):
        y = i * TILESIZE
        pygame.draw.line(screen, WHITE, (0, y), (width, y))

def print_stuff():
    print 'print_stuff'

def draw_player(screen, point):
    x, y = point
    pygame.draw.rect(screen, BLUE, Rect(x,y, TILESIZE,TILESIZE))

def draw_junk(screen, point):
    x, y = point
    pygame.draw.rect(screen, GREEN, Rect(x,y, TILESIZE,TILESIZE))

def draw_laser(screen, point, vert):
    x, y = point
    w = TILESIZE / 2 if vert else TILESIZE
    h = TILESIZE if vert else TILESIZE / 2
    pygame.draw.rect(screen, RED, Rect(x,y, w, h))

def drunk_walk(junk):
    for junk_pos, junk_dir in junk:
        junk_pos[0] += junk_dir[0]
        junk_pos[1] += junk_dir[1]
        if random.random() < 0.15:
            junk_dir[0] = random.randint(-1,1)
            junk_dir[1] = random.randint(-1,1)

def check_collisions(lasers, junk):
    for laser_index, (laser_pos, laser_dir) in enumerate(lasers):
        for junk_index, (junk_pos, junk_dir) in enumerate(junk):
            if abs(laser_pos[0] - junk_pos[0]) < TILESIZE/2 \
            and abs(laser_pos[1] - junk_pos[1]) < TILESIZE / 2:
                lasers.pop(laser_index)
                junk.pop(junk_index)

def sub_vec(mouse, player):
    result = [0,0]
    result[0] = mouse[0] - player[0]
    result[1] = mouse[1] - player[1]
    return result


def unit_vec(direction):
    length = math.sqrt(direction[0]**2 + direction[1]**2)
    result = [0,0]
    result[0] = (1/length) * direction[0]
    result[1] = (1/length) * direction[1]
    return result





if __name__=='__main__':
    pygame.init()

    print_stuff()


    screen = pygame.display.set_mode((320,240))

    rand_point = [random.randint(0,width), random.randint(0,height)]
    print rand_point

    ball = pygame.image.load('ball.gif')
    ballrect = ball.get_rect()
    speed = [2,2]
    player_pos = [50, 50]
    player_speed = [0,0]
    direction = [1,0]

    lasers = []

    randpoints = []
    
    for i in range(10):
        rand_point = [random.randint(0,width), random.randint(0,height)]
        rand_dir = [0,0]
        randpoints.append((rand_point, rand_dir))


    left, up, right, down = False, False, False, False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    sys.exit(0)
                if event.key == K_SPACE:
                    difference = sub_vec(pygame.mouse.get_pos(), player_pos)
                    laser_speed = unit_vec(difference)
                    laser = ([player_pos[0], player_pos[1]],
                                laser_speed) 
                    lasers.append(laser)
                if event.key == K_LEFT:
                    left = True
                    #player_speed[0] = -1
                    
                if event.key == K_RIGHT:
                    right = True
                    #player_speed[0] = 1
                if event.key == K_UP:
                    up = True
                   #player_speed[1] = -1
                if event.key == K_DOWN:
                    down = True
                    #player_speed[1] = 1
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    left = False
                    #player_speed[0] = -1
                    
                if event.key == K_RIGHT:
                    right = False
                    #player_speed[0] = 1
                if event.key == K_UP:
                    up = False
                   #player_speed[1] = -1
                if event.key == K_DOWN:
                    down = False
                    #player_speed[1] = 1
        if (right and not left):
            if player_pos[0] == width:
                player_speed[0] = 0
            else:
                player_speed[0] = 2
        elif (left and not right):
            if player_pos[0] == 0:
                player_speed[0] = 0
            else:
                player_speed[0] = -2
        else:
            player_speed[0] = 0

        if (up and not down):
            if player_pos[1] == 0:
                player_speed[1] = 0
            else:
                player_speed[1]  = -2
        elif (down and not up):
            if player_pos[1] == height:
                player_speed[1] = 0
            else:
                player_speed[1] = 2
        else:
            player_speed[1] = 0

        if (player_speed[0] or player_speed[1]):
            direction[0] = player_speed[0]
            direction[1] = player_speed[1]   

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill((0,0,0))
        screen.blit(ball, ballrect)
        check_collisions(lasers, randpoints)
        drunk_walk(randpoints)
        for junk_pos, junk_dir in randpoints:
            junk_pos[0] += junk_dir[0]
            junk_pos[1] += junk_dir[1]
            draw_junk(screen,junk_pos)

        player_pos[0] += player_speed[0]
        player_pos[1] += player_speed[1]
        draw_player(screen,player_pos)
        for laser_pos, laser_dir in lasers:
            laser_pos[0] += 8*laser_dir[0]
            laser_pos[1] += 8*laser_dir[1]
            draw_laser(screen, laser_pos, laser_dir[1])
        draw_grid(screen)
        pygame.display.flip()
        time.sleep(.05)



    