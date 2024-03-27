import pygame
import os


pygame.init()


screen_width, screen_height = 619, 980
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music")


background = pygame.image.load("music/myphoto.PNG")
background = pygame.transform.scale(background, (screen_width, screen_height))


music_dir = r"c:\Users\bekza\OneDrive\Документы\GitHub\lab7\music"
playlist = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]


current_track = 0
paused = False


pygame.mixer.init()
pygame.mixer.music.load(playlist[current_track])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:  
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:  
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                paused = False

    
    screen.blit(background, (0, 0))

    
    pygame.display.flip()

pygame.quit()
