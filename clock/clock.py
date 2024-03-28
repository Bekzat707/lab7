import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((1400,1050))
pygame.display.set_caption("Часы ")
icon = pygame.image.load("clock/photo.jpg")
pygame.display.set_icon(icon)
fps = 24
background = pygame.image.load("clock/mainclock.png")

clock = pygame.time.Clock()

minhand = pygame.image.load("clock/rightarm.png")
sechand = pygame.image.load("clock/leftarm.png")

minrect = minhand.get_rect()
minrect.center = ((700,525))

secrect =sechand.get_rect()
secrect.center = (700,525)

currenttime = datetime.datetime.now()
secvalue = currenttime.second
minvalue = currenttime.minute

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    genminhand = pygame.transform.rotate(minhand, -1*((6*minvalue+50)%360))
    genminrect = genminhand.get_rect()
    genminrect.center = minrect.center

    screen.blit(genminhand,genminrect)

    gensechand = pygame.transform.rotate(sechand, -1*((6*secvalue+180)%360))
    gensecrect = gensechand.get_rect()
    gensecrect.center = secrect.center

    screen.blit(gensechand, gensecrect)

    currenttime = datetime.datetime.now()
    secvalue = currenttime.second
    minvalue = currenttime.minute

    pygame.display.update()
    clock.tick(fps)

pygame.quit()