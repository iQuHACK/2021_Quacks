import pygame as pg
from pygame.locals import *

#Screen Size
width= 1200
height= 700

pg.display.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Quantum Mystery Flow")

isRunning = True  

card1 = pg.image.load('sprites/sprite1.png')
card1.convert()
card2 = pg.image.load('sprites/sprite2.png')
card2.convert()
card3 = pg.image.load('sprites/sprite3.png')
card3.convert()
card4 = pg.image.load('sprites/sprite4.png')
card4.convert()

rect1 = card1.get_rect()
rect2 = card2.get_rect()
rect3 = card3.get_rect()
rect4 = card3.get_rect()
#Poner la carta 20 pixeles sobre el limite inferior, a.k.a esquina superior en: (largo total) - (largo de carta) - 20
rect1.move_ip(20 - rect1[0], height - 20 - rect1[3] - rect1[1])
rect2.x = rect1.x + 320
rect2.y = rect1.y
rect4.x = width - 220
rect4.y = rect1.y
rect3.x = rect4.x - 320
rect3.y = rect2.y



moving = False

while isRunning:  
    for event in pg.event.get():  
        if event.type == QUIT: 
            isRunning = False 

        elif event.type == MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
            #Regresar a posicion original
            rect1.move_ip(20 - rect1[0], height - 20 - rect1[3] - rect1[1])

        elif event.type == MOUSEMOTION and moving:
            rect1.move_ip(event.rel)
        
        screen.fill((150, 150, 150))
        screen.blit(card1, rect1) 
        screen.blit(card2, rect2) 
        screen.blit(card3, rect3) 
        screen.blit(card4, rect4) 
        pg.display.update()
pg.quit()