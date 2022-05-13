import pygame
from pygame.locals import *
import random
from maze import Maze
from maze_solver import Maze_Solver

size = width, height = 800, 800

bgcolor = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.font.init()

font = pygame.font.SysFont('arial', 20)

running = True

MAZE_SIZE = (16,16)
CELL_SIZE = 40

m = Maze(MAZE_SIZE)
solver = Maze_Solver(m)
sol = []

bx, by  = (80,80)

start = None
end = None
mouse_cell = (0,0)

animating = None
animating_buffer = 0
animation_step = 10
animating_range = (0,170)

while running:
    screen.fill(bgcolor)
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                lx,ly = event.pos
                cx = (lx-bx)//CELL_SIZE
                cy = (ly-by)//CELL_SIZE
                if cx >= 0 and cy >= 0 and cx < MAZE_SIZE[0] and cy < MAZE_SIZE[1]:
                    start = (cx,cy)
                
            if event.button == 2:
                start = None
                end = None
                

            if event.button == 3:
                lx,ly = event.pos
                cx = (lx-bx)//CELL_SIZE
                cy = (ly-by)//CELL_SIZE
                if cx >= 0 and cy >= 0 and cx < MAZE_SIZE[0] and cy < MAZE_SIZE[1]:
                    end = (cx,cy)
                
    lx,ly = pygame.mouse.get_pos()
    cx = (lx-bx)//CELL_SIZE
    cy = (ly-by)//CELL_SIZE
    if cx >= 0 and cy >= 0 and cx < MAZE_SIZE[0] and cy < MAZE_SIZE[1]:
        mouse_cell = (cx,cy)
        if animating == mouse_cell:
            animating_buffer = min(animating_range[1], animating_buffer+animation_step)
        else:
            animating = mouse_cell
            animating_buffer = animating_range[0]
    else:
        animating = None

    if end == None and start == None:
        sol = []
    elif end == None and start != None:
        solver.solve(start, mouse_cell)
        sol = solver.get_solution()
    elif end != None and start == None:
        solver.solve(end, mouse_cell)
        sol = solver.get_solution()
    else:
        solver.solve(start, end)
        sol = solver.get_solution()

    if animating != None:
        pygame.draw.rect(screen, [animating_buffer]*3, pygame.Rect(bx+animating[0]*CELL_SIZE, by+animating[1]*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)
    for x in range(MAZE_SIZE[0]):
        for y in range(MAZE_SIZE[1]):
            if not (x-1, y, x, y) in m.doors and not (x+y==0):
                pygame.draw.line(screen, white, (bx+x*CELL_SIZE, by+y*CELL_SIZE),(bx+x*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x-1, y) in sol and (x,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE - CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2,by+y*CELL_SIZE + CELL_SIZE//2))   

            if not (x,y,x+1,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x+1)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x, y) in sol and (x+1,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + 3*(CELL_SIZE//2),by+y*CELL_SIZE + CELL_SIZE//2))   
                
            if not (x,y-1,x,y) in m.doors:
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+y*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y)*CELL_SIZE))   
            else:
                if (x, y-1) in sol and (x,y) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE - CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2))   
                
            if not (x,y,x,y+1) in m.doors and not (x+y==MAZE_SIZE[0]+MAZE_SIZE[1]-2):
                pygame.draw.line(screen, white, (bx+(x)*CELL_SIZE, by+(y+1)*CELL_SIZE),(bx+(x+1)*CELL_SIZE, by+(y+1)*CELL_SIZE))   
            else:
                if (x, y) in sol and (x,y+1) in sol:
                    pygame.draw.line(screen, (0,255,0), (bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + CELL_SIZE//2),(bx+x*CELL_SIZE + CELL_SIZE//2, by+y*CELL_SIZE + 3*(CELL_SIZE//2)))   

    


    pygame.display.update()
    clock.tick(60)