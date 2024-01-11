import random
import pygame

pygame.init()

width = 700
height = 700
e = 2.71
maxvel = 0
gravityconstant = 5
massofpointer = 50
nparticles = 1000

radiusofpointer = 20
screen = pygame.display.set_mode([width, height])

running = True


class particle:
    def __init__(self,i):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 10
        self.mass = 2
        self.life = 300+i
        self.color = (0, 0, 0)

    def show(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius=2)
        self.life-=1
        if(self.life==0):
            self.generate()

    def generate(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 10
        self.mass = 2
        self.life = 300
        self.color = (0, 0, 0)



    def getpos(self):
        return (self.x,self.y)

    def update(self, x, y):
        # print(self.x - x)
        dist = ((((self.x - x) ** 2) + ((self.y - y) ** 2)) ** 0.5)
        velocity = ((((self.vx) ** 2) + ((self.vy) ** 2)) ** 0.5) * 200 + 100
        if velocity > 3*255:
            velocity = 3*255
        velc = velocity - (256 * 2)
        if velc<=0:
            velc=0
        elif velc>255:
            velc=255
        velb = velocity - (256)
        if velb<=0:
            velb=0
        elif velb>255:
            velb=255
        vela = velocity
        if vela>255:
            vela=255
        if dist <= radiusofpointer:
            dist = radiusofpointer
        distx = x - self.x
        disty = y - self.y
        acc = gravityconstant * self.mass * massofpointer / (dist * dist)
        self.ax = acc * distx / dist
        self.ay = acc * disty / dist
        self.vx = self.vx + self.ax
        self.vy = self.vy + self.ay
        if (self.x >= width):
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
            self.vx = random.randint(0, 1)
            self.vy = random.randint(0, 1)
        if (self.y >= height):
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
            self.vx = random.randint(0, 1)
            self.vy = random.randint(0, 1)
        if (self.x <= 0):
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
            self.vx = random.randint(0, 1)
            self.vy = random.randint(0, 1)
        if (self.y <= 0):
            self.x = random.randint(0, width)
            self.y = random.randint(0, height)
            self.vx = random.randint(0, 1)
            self.vy = random.randint(0, 1)
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        self.vx *= 0.99
        self.vy *= 0.99
        self.color = (vela, velb, velc)


particles = [0] * nparticles

for i in range(nparticles):
    particles[i] = particle(i)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    x, y = width / 2, height / 2
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
    for i in range(nparticles):
        particles[i].show(screen)
        particles[i].update(x, y)
    pygame.draw.circle(screen, "blue", (x, y), radius=10)
#    for i in range(nparticles-1):
#        pygame.draw.line(screen, particles[i].color, particles[i].getpos(), (x,y))
#        pygame.draw.line(screen, particles[i].color, particles[i].getpos(), particles[i+1].getpos())

    pygame.display.flip()


pygame.quit()
