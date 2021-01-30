import pygame as pg

#Screen Size
width= 800
height= 600

pg.display.init()   
screen = pg.display.set_mode((width,height))  
screen.fill((255,255,255))
isRunning = True  

while isRunning:  
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            isRunning = False  
        pg.display.update()
