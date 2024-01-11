import pygame
# importing request library
import requests

# setting up the width and the background color of the window
WIDTH = 550
background_color = (38, 38, 38)
original_grid_element_color = (255, 255, 255)
buffer = 5
#adding API in our sudoku game
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
#adding the functionality that can add the number on user bases
def insert(win, position):
    i,j = position[1], position[0]
    #adding the font and its size
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                   
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): #checking with 0
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #We are checking for valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (179, 179, 179))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return
              def main():   
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH)) # creating the window
    pygame.display.set_caption("Sudoku")#giving caption
    win.fill(background_color) # filling the window with background color
    myfont = pygame.font.SysFont('Comic Sans MS', 35)  #adding the font and its size
    # creating grid
    for i in range(0,10):
        if(i%3 == 0):
            #drwaing the block line (vertical)
            pygame.draw.line(win, (255, 255, 255), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            #(Horizontal)
            pygame.draw.line(win, (255, 255, 255), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        #drwaing vertical line
        pygame.draw.line(win, (166, 166, 166), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        #drwaing horizental line
        pygame.draw.line(win, (166, 166, 166), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
   
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
    #adding the function that if we press the quit key then the pygame window will close.   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
 
main()
