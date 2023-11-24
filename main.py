import pygame, sys

# setup
pygame.init()
clock =  pygame.time.Clock()

# Setup window
WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

ball = pygame.Rect(WIDTH/2 -15, HEIGHT/2 -15,30,30)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70,10,140)
opponent = pygame.Rect(10, HEIGHT/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    # updating the window
    pygame.display.flip()
    clock.tick(60)