import pygame

class Square:
    def __init__(self, mass, velocity, xPos, yPos):
        self.mass = mass
        self.velocity = velocity
        self.xPos = xPos
        self.yPos = yPos
        self.size = mass * 10

    def move(self):
        self.xPos += self.velocity

    def checkCollides(a, b):
        if abs(a.xPos - b.xPos) < (a.size + b.size) / 2:
            a.handleCollide(b)
        a.handleWall()
        b.handleWall()

    def handleCollide(self, b):
        v1 = ((self.mass - b.mass) * self.velocity + 2 * b.mass * b.velocity) / (self.mass + b.mass)
        v2 = ((b.mass - self.mass) * b.velocity + 2 * self.mass * self.velocity) / (self.mass + b.mass)
        self.velocity = v1
        b.velocity = v2

    def handleWall(self):
        if self.xPos + self.size / 2 >= 800 or self.xPos - self.size / 2  <= 0:
            self.velocity *= -1

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Collisions")
clock = pygame.time.Clock()

mass1 = int(input("What is the mass of object one? "))
velo1 = int(input("What is the velocity of object one? "))
mass2 = int(input("What is the mass of object two? "))
velo2 = int(input("What is the velocity of object two? "))

obj1 = Square(mass1, velo1, 100, 175)
obj2 = Square(mass2, velo2 * -1, 650, 175)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill((15, 15, 30))
    pygame.draw.rect(screen, (70, 130, 255), (obj1.xPos - obj1.size / 2, obj1.yPos - obj1.size / 2, obj1.size, obj1.size,))
    pygame.draw.rect(screen, (255, 100, 70), (obj2.xPos - obj2.size / 2, obj2.yPos - obj2.size / 2, obj2.size, obj2.size))
    pygame.display.flip()
    Square.checkCollides(obj1, obj2)
    obj1.move()
    obj2.move()

pygame.quit()