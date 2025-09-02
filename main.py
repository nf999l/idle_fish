import pygame
import sys

#kaufmenu für fische


pygame.init() #initialisieren pygame
#hintergrund muss erstellt werden mit den tiles
screen = pygame.display.set_mode(([1600, 900]))
pygame.display.set_caption("Fish Idle")
timer = pygame.time.Clock()
framerate = 60 #60fps
time = 0 #um sekunden zu erfassen

class generator:
    def __init__(self):
        ...
    def update(self):
        ...

class ressource:
    def __init__(self):
        ...

class fish:
    def __init__(self):
        ...



running = True
while running:
    timer.tick(framerate) #kurzversion für pygame.time.Clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #sekunden erfassen
    time += 1
    if time >= 60:
        time = 0
        print("1 Sekunde vergangen")
        generator.update()
    #-----------------

pygame.quit()
