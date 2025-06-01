import pygame, time
pygame.mixer.init()
pygame.mixer.music.load('AXTY.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)