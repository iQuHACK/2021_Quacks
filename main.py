import pygame as pg
from pygame.locals import *

#Screen Size
width= 1200
height= 700

pg.display.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Quantum Mystery Flow")

def menu_principal():
    menuRunning = True
    while menuRunning:
        screen.fill((0, 0, 0))

        button_play = pg.Rect(50, height/2, 150, 50)
        pg.draw.rect(screen, (102, 178, 255), button_play)

        for event in pg.event.get():
            if event.type == QUIT:
                menuRunning = False 

            elif event.type == MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    juego()
        
        pg.display.update()

def juego():
    isRunning = True  

    card1 = pg.image.load('sprites/sprite1.png').convert()
    card2 = pg.image.load('sprites/sprite2.png').convert()
    card3 = pg.image.load('sprites/sprite3.png').convert()
    card4 = pg.image.load('sprites/sprite4.png').convert()

    rect1 = card1.get_rect()
    rect2 = card2.get_rect()
    rect3 = card3.get_rect()
    rect4 = card4.get_rect()

    #Poner la carta 20 pixeles sobre el limite inferior, a.k.a esquina superior en: (largo total) - (largo de carta) - 20
    rect1.move_ip( (20 - rect1[0]), (height - 20 - rect1[3] - rect1[1]) ) 
    rect2.x = rect1.x + 320
    rect2.y = rect1.y
    rect4.x = width - 220
    rect4.y = rect1.y
    rect3.x = rect4.x - 320
    rect3.y = rect1.y

    moving = [0, 0, 0, 0]

    while isRunning:  
        for event in pg.event.get():  
            if event.type == QUIT: 
                isRunning = False 

            elif event.type == MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    moving = [1, 0, 0, 0]
                elif rect2.collidepoint(event.pos):
                    moving = [0, 1, 0, 0]
                elif rect3.collidepoint(event.pos):
                    moving = [0, 0, 1, 0]
                elif rect4.collidepoint(event.pos):
                    moving = [0, 0, 0, 1]

            elif event.type == MOUSEBUTTONUP:
                #Regresar a posicion original, si es que algo se estaba moviendo
                if sum(moving)>0:
                    rect1.move_ip(20 - rect1[0], height - 20 - rect1[3] - rect1[1])
                    rect2.x = rect1.x + 320
                    rect2.y = rect1.y
                    rect4.x = width - 220
                    rect4.y = rect1.y
                    rect3.x = rect4.x - 320
                    rect3.y = rect1.y
                #Desactivar movimiento
                moving = [0, 0, 0, 0]

            elif event.type == MOUSEMOTION:
                if moving[0]:
                    rect1.move_ip(event.rel)
                elif moving[1]:
                    rect2.move_ip(event.rel)
                elif moving[2]:
                    rect3.move_ip(event.rel)
                elif moving[3]:
                    rect4.move_ip(event.rel)
        
            screen.fill((150, 150, 150))
            screen.blit(card1, rect1) 
            screen.blit(card2, rect2) 
            screen.blit(card3, rect3) 
            screen.blit(card4, rect4) 
            pg.display.update()

menu_principal()

pg.quit()