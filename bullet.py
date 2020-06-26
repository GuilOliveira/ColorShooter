import pygame as pg
import player
import math


def shootCalc(oldX, oldY, speed, angle):
    new_x = oldX + speed * math.cos(angle)
    new_y = oldY + speed * math.sin(angle)
    return new_x, new_y


def clock():
    current_time = pg.time.get_ticks()
    return current_time


class Bullet(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.slope = 0
        self.image = pg.image.load("data/shoot.png")
        self.image = pg.transform.scale(self.image, [10, 10])
        self.rect = [0, 0, 10, 10]
        self.firstTime = True

        self.speed = 5

    def update(self):

        if self.firstTime:
            self.actualdx = self.rect[0] - pg.mouse.get_pos()[0]
            self.actualdy = self.rect[1] - pg.mouse.get_pos()[1]
            self.actualx = self.rect[0]
            self.actualy = self.rect[1]
            self.mousex = pg.mouse.get_pos()[0]
            self.mousey = pg.mouse.get_pos()[1]
            self.firstTime = False
            self.startTime = clock() + 1000
            offset = (self.mousey - self.actualy, self.mousex - self.actualx)
            self.angle = -math.radians(135 - math.degrees(math.atan2(*offset)) - 135)

        if (self.actualdy and self.actualx) == 0:
            self.kill()

            pass

        self.rect[0], self.rect[1] = shootCalc(self.rect[0], self.rect[1], self.speed, self.angle)

        if clock() > self.startTime + 700:
            self.kill()
        pass
