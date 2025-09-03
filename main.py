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

#create player with playerdata
playerData = {}
file = open("savegame/savegame.txt", "r")
playerData = file.read() #wenn das nicht funktioniert muss ich die daten splitten
file.close()
#-----------------------------
class player:
    def __init__(self):
        self.name = playerData["name"]
        self.balance = playerData["balance"] 
        
class generator:
    def __init__(self):
        ...
        #balance
        #fish1 anzahl
        #fish2 anzahl  usw.  
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
        generator.update() #ädnern in neuen code
    #-----------------

pygame.quit()
