import pygame as pg
from pygame.locals import *
import random
from array import *
import TEST

#Colors
color_background = (0, 0, 0)
color_button = (255, 255, 255)
#(102, 178, 255)

#Screen Size
width= 1200
height= 700

pg.init()

pg.display.init()
screen = pg.display.set_mode((width,height))
pg.display.set_caption("Quantum Mystery Flow")

#Fonts
font_small = pg.font.SysFont(None, 24)
font_medium = pg.font.SysFont(None, 48)
font_big = pg.font.SysFont(None, 96)

def menu_principal():
    menuRunning = True
    while menuRunning:
        screen.fill(color_background)

        button_play = pg.Rect(50, height/2, 150, 50)
        button_credits = pg.Rect(50, height/2 + 75, 150, 50)
        button_quit = pg.Rect(50, height/2 + 150, 50, 50)
        pg.draw.rect(screen, color_button, button_play)
        pg.draw.rect(screen, color_button, button_credits)
        pg.draw.rect(screen, color_button, button_quit)

        txt_titulo = font_big.render('Quantum Mystery Flow', True, color_button)
        txt_subtitulo = font_small.render('Name pending approval uwu', True, color_button)
        txt_play = font_medium.render('P L A Y', True, color_background)
        txt_credits = font_medium.render('Credits', True, color_background)
        txt_quit = font_medium.render('x', True, color_background)

        for event in pg.event.get():
            if event.type == QUIT:
                menuRunning = False 

            elif event.type == MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    juego()

                elif button_quit.collidepoint(event.pos):
                	menuRunning = False

                elif button_credits.collidepoint(event.pos):
                	creditos()
        
        screen.blit(txt_titulo, (width/2 - txt_titulo.get_rect()[2]/2, 50))
        screen.blit(txt_subtitulo, (width/2 - txt_subtitulo.get_rect()[2]/2, 150))
        screen.blit(txt_play, (125 - txt_play.get_rect()[2]/2, height/2 + 25 - txt_play.get_rect()[3]/2))
        screen.blit(txt_credits, (125 - txt_credits.get_rect()[2]/2, height/2 + 100 - txt_credits.get_rect()[3]/2))
        screen.blit(txt_quit, (75 - txt_quit.get_rect()[2]/2, height/2 + 175 - txt_quit.get_rect()[3]/2))
        #coord x_txt = coord x_btn + width_btn/2 - width_txt/2
        #coord y_txt = coord y_btn + height_btn/2 - height_txt/2
        pg.display.update()

def juego():
    isRunning = True  

    card1 = pg.image.load('sprites/sprite1.png').convert()
    card2 = pg.image.load('sprites/sprite2.png').convert()
    card3 = pg.image.load('sprites/sprite3.png').convert()
    card4 = pg.image.load('sprites/sprite4.png').convert()
    card5 = pg.image.load('sprites/sprite5.png').convert()

    #randomizar -> card[]
    card = [card1, card2, card3, card4, card5]
    random.shuffle(card)

    rect1 = card[0].get_rect()
    rect2 = card[1].get_rect()
    rect3 = card[2].get_rect()
    rect4 = card[3].get_rect()

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
        screen.fill((150, 150, 150))

        button_back = pg.Rect(50, 20, 100, 50)
        pg.draw.rect(screen, color_background, button_back)
        txt_back = font_medium.render('Back', True, color_button)

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
                elif button_back.collidepoint(event.pos):
                	isRunning = False

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
        
            screen.blit(txt_back, (100 - txt_back.get_rect()[2]/2, 45 - txt_back.get_rect()[3]/2))
            screen.blit(card[0], rect1)
            screen.blit(card[1], rect2)
            screen.blit(card[2], rect3)
            screen.blit(card[3], rect4)
            pg.display.update()

def creditos():
    creditsRunning = True
    while creditsRunning:
        screen.fill(color_background)

        button_back = pg.Rect(50, 20, 100, 50)
        pg.draw.rect(screen, color_button, button_back)

        txt_back = font_medium.render('Back', True, color_background)
        txt_team = font_big.render('Game by team Quacks', True, color_button)
        txt_Lalo = font_medium.render('Eduardo Martínez', True, color_button)
        txt_Tanya = font_medium.render('Tanya Gonzalez', True, color_button)
        txt_Alan = font_medium.render('Alan Anaya', True, color_button)
        txt_Willy = font_medium.render('Guillermo Saenz', True, color_button)

        for event in pg.event.get():
            if event.type == QUIT:
                creditsRunning = False

            elif event.type == MOUSEBUTTONDOWN and button_back.collidepoint(event.pos):
                creditsRunning = False

        screen.blit(txt_back, (100 - txt_back.get_rect()[2]/2, 45 - txt_back.get_rect()[3]/2))
        screen.blit(txt_team, (50, 200))
        screen.blit(txt_Lalo, (50, 300))
        screen.blit(txt_Tanya, (50, 350))
        screen.blit(txt_Alan, (50, 400))
        screen.blit(txt_Willy, (50, 450))
        pg.display.update()

menu_principal()

pg.quit()

#Arreglos:
#	Cartas random
#	Cuando se arrastre la carta, desaparecerla
#	Fondo bonito
#	Completar opciones del menu(?)