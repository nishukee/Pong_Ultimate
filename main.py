# importing the pygame library and initialise game engine
import pygame as pg
from paddle import Paddle
pg.init()

# defining colors used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# open the game window
size = (700, 500)
screen = pg.display.set_mode(size)
pg.display.set_caption("PONG")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

all_sprites_list = pg.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# This loop will carry on until the user exits the game
carryOn = True

# clock is used to control how fast the screen updates
clock = pg.time.Clock()

# _______Main Program Loop_______
while carryOn:
    # ____Main event loop___
    for event in pg.event.get():  # User did something(event)
        if event.type == pg.QUIT:  # If user clicked close
            carryOn = False    # Flag to say we are done with the game and exit the loop

    all_sprites_list.update()

    screen.fill(BLACK)
    pg.draw.line(screen, WHITE, [350, 0], [350, 500], 5)
    pg.display.flip()
    clock.tick(60)
pg.quit()
