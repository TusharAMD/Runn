import pygame as pg
import pygame.gfxdraw
import sys,os,math

pg.init()
pg.event.set_allowed([pg.QUIT,pg.MOUSEMOTION,pg.MOUSEBUTTONDOWN,pg.KEYDOWN])


clock = pygame.time.Clock()
fps = 120
font = pg.font.SysFont('consolas',20)
screenres = (500,500)
realres = (screenres[0]*1.2,screenres[1]*1.2)

updated = False
dirtyrects = []


clear =  (  0,  0,  0,  0)
white =  (255,255,255)
gray =   (150,150,150)
black =  (  0,  0,  0)
red =    (255,  0,  0)
orange = (255,125,  0)
yellow = (255,255,  0)
green =  (  0,225,  0)
blue =   (  0,  0,255)
purple = (150,  0,150)

colors = [black,white,red,orange,yellow,green,blue,purple]

numkey = [
    pg.K_1,
    pg.K_2,
    pg.K_3,
    pg.K_4,
    pg.K_5,
    pg.K_6,
    pg.K_7,
    pg.K_8
]


window = pg.display.set_mode(screenres,pg.DOUBLEBUF)
window.fill(white)
canvas = pg.Surface((realres[0],realres[1]*0.84)).convert_alpha()
canvas.fill(white)
latest1 = canvas.copy()
latest2 = canvas.copy()
latest3 = canvas.copy()
latest4 = canvas.copy()
latest5 = canvas.copy()
layers = [latest1,latest2,latest3,latest4,latest5]
for layer in layers:
    layer.fill(clear)
overlay = pg.Surface(screenres).convert_alpha()


realrect = pg.Rect(0,0,realres[0],int(realres[1]*0.84))
screenrect = pg.Rect(0,0,screenres[0],int(screenres[1]*0.84))
toolbar = pg.Rect(0,420,500,80)

r = 25
clr = black
startpoint = None
endpoint = None
ongoing = False
undone = 0
maxundone = 0
holdingclick = False

def button(color,rect):
    global clr,holdingclick
    if 0 <= rect <= 9:
        rect = pg.Rect(48*rect+12,446,44,44)
        if pg.mouse.get_pressed()[0] and rect.collidepoint(mousepos) and not holdingclick:
            clr = color
            dirtyrects.append(toolbar)
        if clr == color:
            pg.draw.rect(overlay,color,rect)
            pg.draw.rect(overlay,black,rect,3)
        else:
            pg.draw.rect(overlay,color,(rect[0]+4,rect[1]+4,rect[2]-8,rect[3]-8))
            pg.draw.rect(overlay,black,(rect[0]+4,rect[1]+4,rect[2]-8,rect[3]-8),3)

def drawline():
    global startpoint,endpoint,start
    if startpoint == None:
        startpoint = x,y
    endpoint = x,y
    if r > 1:
        if startpoint != endpoint:
            dx,dy = endpoint[0]-startpoint[0],endpoint[1]-startpoint[1]
            angle = math.atan2(-dy,dx)%(2*math.pi)
            dx,dy = math.sin(angle)*(r*0.999),math.cos(angle)*(r*0.999)
            a = startpoint[0]+dx,startpoint[1]+dy
            b = startpoint[0]-dx,startpoint[1]-dy
            c = endpoint[0]-dx,endpoint[1]-dy
            d = endpoint[0]+dx,endpoint[1]+dy
            pointlist = [a,b,c,d]
            pg.draw.polygon(latest1,clr,pointlist)
        pg.draw.circle(latest1,clr,(x,y),r)
    else:
        pg.draw.line(latest1,clr,startpoint,endpoint,r)
    startpoint = x,y

def shiftdown():
    for layer in reversed(layers):
        if layer == latest5:
            canvas.blit(latest5,(0,0))
        else:
            layers[layers.index(layer)+1].blit(layer,(0,0))

def shiftup():
    for layer in layers:
        if layer == latest5:
            layer.fill(clear)
        else:
            layer.fill(clear)
            layer.blit(layers[layers.index(layer)+1],(0,0))


overlay.fill(clear)
pg.draw.rect(overlay,gray,toolbar)
pg.draw.rect(overlay,black,toolbar,3)

for color in colors:
    text = font.render(str(colors.index(color)+1),True,black)
    overlay.blit(text,(48*colors.index(color)+28,424))

overlaybg = overlay.copy()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEMOTION:
            mousepos = pg.mouse.get_pos()
            x = int(mousepos[0]*(realres[0]/screenres[0]))
            y = int(mousepos[1]*(realres[1]/screenres[1]))
            holdingclick = True
            if screenrect.collidepoint(mousepos):
                dirtyrects.append(screenrect)

        if event.type == pg.MOUSEBUTTONDOWN:
            holdingclick = False
            if screenrect.collidepoint(mousepos):
                dirtyrects.append(screenrect)

           
            if event.button == 4 and r < 100:
                r += 1
                dirtyrects.append(screenrect)
            elif event.button == 5 and r > 2:
                r -= 1
                dirtyrects.append(screenrect)

        if event.type == pg.KEYDOWN:

            if event.key in numkey:
                clr = colors[numkey.index(event.key)]
                dirtyrects.append(toolbar)

         
            if event.key == pg.K_e:
                canvas.fill(white)
                latest5.fill(clear)
                latest4.fill(clear)
                latest3.fill(clear)
                latest2.fill(clear)
                latest1.fill(clear)
                undone = 0
                maxundone = 0
                dirtyrects.append(screenrect)

        
            if event.key == pg.K_u and undone < maxundone:
                undone += 1
                dirtyrects.append(screenrect)
            if event.key == pg.K_i and undone > 0:
                undone -= 1
                dirtyrects.append(screenrect)


    if pg.mouse.get_pressed()[0] and screenrect.collidepoint(mousepos):
        if not ongoing:
            while undone > 0:
                shiftup()
                undone -= 1
                maxundone -= 1
            shiftdown()
        drawline()
        ongoing = True
    else:
        startpoint = None
        if ongoing:
            if maxundone < 5:
                maxundone += 1
            ongoing = False

    if screenrect in dirtyrects:
        window.fill(white)
        for layer in layers:
            if layers.index(layer) == undone:
                window.blit(pg.transform.smoothscale(layer,(screenrect[2],screenrect[3])),screenrect)
        overlay.fill(clear)
        if r > 1:
            pg.gfxdraw.aacircle(overlay,mousepos[0],mousepos[1],int(r*screenres[0]/realres[0]),gray)
    overlay.blit(overlaybg,screenrect)
    for color in colors:
        button(color,colors.index(color))
    window.blit(overlay,screenrect)

    pg.display.set_caption('Draw   |   FPS: ' + str(int(clock.get_fps())))
    clock.tick(fps)

   
    if not updated:
        pg.display.update()
        updated = True
    pg.display.update(dirtyrects)
    dirtyrects.clear()