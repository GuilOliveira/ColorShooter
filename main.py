import pygame as pg
import colorloop as cl
import player



pg.init()
# DISPLAY SETUP
ScreenW = 1360
ScreenH = 765
# display = pg.display.set_mode([ScreenW, ScreenH])
display = pg.display.set_mode([ScreenW, ScreenH], pg.DOUBLEBUF)

pg.display.set_caption("build teste nem alpha é kkkkkkk")
clock = pg.time.Clock()


def draw():
    display.fill([120, 120, 120])


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

# GAMELOOP
gameloop = True
while gameloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameloop = False
    time = clock.tick(110)

    #r, g, b, rCheck, gCheck, bCheck = cl.ColorLoop(r, g, b, rCheck, gCheck, bCheck)
    x = pg.mouse.get_pos()[0]
    y = pg.mouse.get_pos()[1]
    print(x, y)
    draw()
    # pg.draw.rect(display, [r, g, b], [ScreenW / 2 - 50, ScreenH / 2 - 50, 100, 100])
    playerGroup.update()
    playerGroup.draw(display)
    pg.display.flip()
