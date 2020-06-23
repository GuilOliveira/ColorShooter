import pygame as pg
import player
playerx = player.playerx
playery = player.playery

def functionBullet(self):
    if pg.mouse.get_pos()[0] - playerx == 0:
        slope = 0
    else:
        slope = (pg.mouse.get_pos()[1] - playery) / (pg.mouse.get_pos()[0] - playerx)
    return slope, pg.mouse.get_pos()[0], playerx, playery, True

class Bullet(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.slope, self.xbullet, self.xplayer, self.yplayer, self.done = functionBullet(self)
        self.image = pg.image.load("data/shoot.png")
        self.image = pg.transform.scale(self.image, [10, 10])
        self.rect = [playerx, playery, 10, 10]
        self.done = False
        print("bbb")

        self.speed = 1
    def update(self):
        self.rect[1] = playery + (self.slope * (self.xbullet - self.xplayer) + self.yplayer)
        self.rect[0] = playerx + (self.xbullet)
        #self.rect[1] += self.ybullet
        self.xbullet += self.speed
        print(playerx, playery)


        pass

