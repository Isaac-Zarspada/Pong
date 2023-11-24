import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH/2, HEIGHT/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
# setup
pygame.init()
clock =  pygame.time.Clock()

# Setup window
TICKSPEED = 38
WIDTH = 1280
HEIGHT = 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# main components
ball = pygame.Rect(WIDTH/2 -15, HEIGHT/2 -15,30,30)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70,10,140)
opponent = pygame.Rect(10, HEIGHT/2 - 70,10,140)

# colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# starting velocity
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# corner idea
triangle1 = [(0, HEIGHT), (0, (HEIGHT-40)), (40, HEIGHT)]
triangle2 = [(0, 0), (0, 40), (40, 0)]
triangle3 = [(WIDTH, 0), (WIDTH, 40), ((WIDTH-40),0)]
triangle4 = [(WIDTH, HEIGHT), (WIDTH, (HEIGHT-40)), ((WIDTH-40), HEIGHT)]
corners = [triangle1,triangle2,triangle3, triangle4]

# score
score = 0
score_surf = pygame.font.Font(None, 50).render('My Score', False, light_grey)
score_rect = score_surf.get_rect(center = (WIDTH / 2 - 30, 50))


while True:
    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:    
                player_speed += 7
            if event.key == pygame.K_UP:    
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:    
                player_speed -= 7
            if event.key == pygame.K_UP:    
                player_speed += 7
            
    ball_animation()
    player_animation()
    opponent_animation()

    # score counter
    

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen,light_grey, (WIDTH/2,0), (WIDTH/2,HEIGHT))
    # Draw the triangle
    for triangle in corners:
        pygame.draw.polygon(screen, (light_grey), triangle)
        
    # updating the window
    pygame.display.flip()
    clock.tick(TICKSPEED)