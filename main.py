import pygame as pg
import colorloop as cl
import player
from settings import *
import bullet

pg.init()
# DISPLAY SETUP

display = pg.display.set_mode([screenW, screenH], pg.DOUBLEBUF)
pg.display.set_caption(title)
clock = pg.time.Clock()


def draw():
    display.fill([70, 70, 70])
    tilemap()


# COLORLOOP VARIABLES
r = 0
g = 0
b = 0
rCheck = True
gCheck = True
bCheck = True

# PLAYER GROUP
playerGroup = pg.sprite.Group()
player = player.Player()
playerGroup.add(player)
bulletGroup = pg.sprite.Group()

def tilemap():
    for x in range(0, screenW, tilesize):
        pg.draw.line(display, [140, 140, 140], (x, 0), (x, screenH))
    for y in range(0, screenH, tilesize):
        pg.draw.line(display, [140, 140, 140], (0, y), (screenW, y))




# GAMELOOP
gameloop = True
while gameloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameloop = False

    time = clock.tick(90)
    if pg.mouse.get_pressed() == (1, 0, 0):
        newBullet = bullet.Bullet(bulletGroup, playerGroup)
    # r, g, b, rCheck, gCheck, bCheck = cl.ColorLoop(r, g, b, rCheck, gCheck, bCheck)
    #x = pg.mouse.get_pos()[0]
    #y = pg.mouse.get_pos()[1]
    #print(x, y)


    draw()
    # pg.draw.rect(display, [r, g, b], [ScreenW / 2 - 50, ScreenH / 2 - 50, 100, 100])
    playerGroup.update()
    bulletGroup.draw(display)
    playerGroup.draw(display)
    pg.display.flip()
    print(player.posX() , player.posY())
