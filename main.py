import pygame, sys

# setup
pygame.init()
clock =  pygame.time.Clock()

# Setup window
WIDTH = 1280
HEIGHT = 960
scren = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

while True:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # updateing the window
    pygame.display.flip()
    cloc