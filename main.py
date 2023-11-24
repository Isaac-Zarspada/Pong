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

ball_speed_x = 7
ball_speed_y = 7


while True:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen,light_grey, (WIDTH/2,0), (WIDTH/2,HEIGHT))

    # updating the window
    pygame.display.flip()
    clock.tick(60)