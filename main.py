import pygame as pg
from pygame.locals import *

#Screen Size
width= 1200
height= 700

pg.display.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Quantum Mystery Flow")
#screen.fill((255,255,255))
isRunning = True  

card1 = pg.image.load('sprites/sprite1.png')
card1.convert()
rect = card1.get_rect()
#Poner la carta 20 pixeles sobre el limite inferior, a.k.a esquina superior en: (largo total) - (largo de carta) - 20
rect.move_ip(20 - rect[0], height - 20 - rect[3] - rect[1])
moving = False

while isRunning:  
    for event in pg.event.get():  
        if event.type == QUIT: 
            isRunning = False 

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
            #Regresar a posicion original
            rect.move_ip(20 - rect[0], height - 20 - rect[3] - rect[1])

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
        
        screen.fill((150, 150, 150))
        screen.blit(card1, rect) 
        pg.display.update()
pg.quit()