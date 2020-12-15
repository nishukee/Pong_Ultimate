# importing the pygame library and initialise game engine
import pygame as pg
from paddle import Paddle
from ball import Ball
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

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pg.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# This loop will carry on until the user exits the game
carryOn = True

# clock is used to control how fast the screen updates
clock = pg.time.Clock()

scoreA = 0
scoreB = 0

# _______Main Program Loop_______
while carryOn:
    # ____Main event loop___
    for event in pg.event.get():  # User did something(event)
        if event.type == pg.QUIT:  # If user clicked close
            carryOn = False    # Flag to say we are done with the game and exit the loop
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                carryOn = False

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        paddleA.moveUp(5)
    if keys[pg.K_s]:
        paddleA.moveDown(5)
    if keys[pg.K_UP]:
        paddleB.moveUp(5)
    if keys[pg.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pg.sprite.collide_mask(ball, paddleA) or pg.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pg.draw.line(screen, WHITE, [350, 0], [350, 500], 5)
    all_sprites_list.draw(screen)

    font = pg.font.Font(None, 74)
    text = font.render(str(scoreA), True, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), True, WHITE)
    screen.blit(text, (420, 10))

    pg.display.flip()
    clock.tick(60)
pg.quit()
