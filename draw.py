import pygame
import sys


pygame.init()


screen_width, screen_height = 900, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_speed = 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - ball_speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_y = min(ball_y + ball_speed, screen_height - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_x - ball_speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + ball_speed, screen_width - ball_radius)

    
    screen.fill(WHITE)

    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)
