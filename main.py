#importing the pygame library and initialise game engine
import pygame as pg
pg.init()

#defining colors used in the game
BLACK = (0,0,0)
WHITE = (255,255,255)

#open the game window
size = (700,500)
screen = pg.display.set_mode(size)
pg.display.set_caption("PONG")

#This loop will carry on until the user exits the game
carrryOn = True

#clock is used to control how fast the screen updates
clock = pg.time.Clock()

#_______Main Program Loop_______
while carrryOn:
    #____Main event loop___
    for event in pg.event.get():  # User did something(event)
        if event.type == pg.QUIT: # If user clicked close
            carrryOn = False    #Flag to say we are done with the game and exit the loop

    screen.fill(BLACK)
    pg.draw.line(screen, WHITE, [350,0], [350,500], 5)
    pg.display.flip()
    clock.tick(60)
pg.quit()