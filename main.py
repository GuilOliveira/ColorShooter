import pygame as pg
import colorloop as cl
import player
from settings import *
import bullet

pg.init()
# DISPLAY SETUP

display = pg.display.set_mode([screenW, screenH], pg.DOUBLEBUF)
captions = title()
clock = pg.time.Clock()


def draw():
    display.blit(grass, (0, 0))
    display.blit(stone, (0, 0))

    # tilemap()


def ct():
    current_time = pg.time.get_ticks()
    return current_time

# COIN GUI
coins = 100
coinFont = pg.font.Font("data/fonts/pixelFont.TTF", 30)
coinImg = pg.image.load("data/skullCoin.png")
coinImg = pg.transform.scale(coinImg, [40, 40])

def coinDraw():
    display.blit(coinImg, (5, 40))
    coin = coinFont.render(str(coins), 1, (251, 242, 54))
    display.blit(coin, (50, 47))

# HEALTH BAR
def healthbar():
    pg.draw.rect(display, (0, 0, 0), (5, 5, 270, 30))
    pg.draw.rect(display, (230, 0, 0), (5, 5, 210, 30))

# COLORLOOP VARIABLES
r = 0
g = 0
b = 0
rCheck = True
gCheck = True
bCheck = True

# PLAYER GROUP

guy = player.Player()
playerGroup = pg.sprite.Group(guy)
bulletGroup = pg.sprite.Group()
ufo = player.Ufo()
ufoGroup = pg.sprite.Group(ufo)
grass = pg.image.load("data/Tiles/grama.png").convert_alpha()
grass = pg.transform.scale(grass, [8000, 8000])
stone = pg.image.load("data/Tiles/pedras.png").convert_alpha()
stone = pg.transform.scale(stone, [8000, 8000])



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
    ufo.rect.center = guy.rect.center
    ufo.rect[1] -= 45
    if pg.mouse.get_pressed() == (1, 0, 0):
        newBullet = bullet.Bullet(bulletGroup)
        newBullet.rect[0], newBullet.rect[1] = ufo.rect.center

    pg.display.set_caption("{} - FPS: {:.2f}".format("Test Build - ColorShooter", clock.get_fps()))
    time = clock.tick(90)

    # r, g, b, rCheck, gCheck, bCheck = cl.ColorLoop(r, g, b, rCheck, gCheck, bCheck)
    # x = pg.mouse.get_pos()[0]
    # y = pg.mouse.get_pos()[1]
    # print(x, y)

    draw()


    # pg.draw.rect(display, [r, g, b], [ScreenW / 2 - 50, ScreenH / 2 - 50, 100, 100])
    playerGroup.update()
    bulletGroup.update()
    ufoGroup.update()
    playerGroup.draw(display)
    bulletGroup.draw(display)
    ufoGroup.draw(display)
    coinDraw()
    healthbar()
    pg.display.flip()
