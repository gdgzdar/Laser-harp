import pygame, time

pygame.init()

try:
    sound = pygame.mixer.Sound("../sounds/sound1.wav")
    sound.play(loops=-1)
except pygame.geterror(), message:
    print("error")

time.sleep(10)