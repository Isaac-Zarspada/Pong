import pygame, sys

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
triangle1 = [(0, 400), (0, 360), (40, 400)]
triangle2 = [(0, 0), (0, 40), (40, 0)]
triangle3 = [(WIDTH, 0), (WIDTH, 40), ((WIDTH-40),0)]
triangle4 = [(WIDTH, HEIGHT), (WIDTH, 360), ((WIDTH-40), HEIGHT)]
corners = [triangle1,triangle2,triangle3, triangle4]
light_grey = (200,200,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the triangle
    for triangle in corners:
        pygame.draw.polygon(screen, (light_grey), triangle)

    pygame.display.update()