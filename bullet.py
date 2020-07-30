import pygame as pg
import player
import math

pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.init()

def shootCalc(oldX, oldY, speed, angle):
    new_x = oldX + speed * math.cos(angle)
    new_y = oldY + speed * math.sin(angle)
    return new_x, new_y

shootSound = pg.mixer.Sound("data/sound/shoot.wav")
shootSound.set_volume(0.2)

def clock():
    current_time = pg.time.get_ticks()
    return current_time
global shoottime
shoottime = clock()

class Bullet(pg.sprite.Sprite):
    def __init__(self, *groups):
        global shoottime
        pg.sprite.Sprite.__init__(self, *groups)
        self.slope = 0
        self.image = pg.image.load("data/shoot.png")
        self.image = pg.transform.scale(self.image, [11, 11])
        self.rect = [0, 0, 11, 11]
        self.firstTime = True

        self.speed = 4
        if clock() > shoottime + 200:
            self.notShoot = False
            shoottime = clock() + 200
            shootSound.play()
        else:
            self.notShoot = True

    def update(self):
        if self.notShoot:
            self.kill()
            pass
        if self.firstTime:
            self.actualx = self.rect[0] + 5
            self.actualy = self.rect[1] + 5
            self.mousex = pg.mouse.get_pos()[0]
            self.mousey = pg.mouse.get_pos()[1]
            self.firstTime = False
            self.startTime = clock()
            offset = (self.mousey - self.actualy, self.mousex - self.actualx)
            self.angle = -math.radians(135 - math.degrees(math.atan2(*offset)) - 135)


        if (self.actualy== 0 and self.actualx== 0):
            self.kill()

            pass

        self.rect[0], self.rect[1] = shootCalc(self.rect[0], self.rect[1], self.speed, self.angle)

        if clock() > self.startTime + 3200:
            self.kill()
        pass

"""
import pygame as pg
import player
import math

canshoot = True

def shootCalc(oldX, oldY, speed, angle):
    new_x = oldX + speed * math.cos(angle)
    new_y = oldY + speed * math.sin(angle)
    return new_x, new_y


def clock():
    current_time = pg.time.get_ticks()
    return current_time
global shoottime
shoottime = clock()

class Bullet(pg.sprite.Sprite):
    def __init__(self, *groups):
        global shoottime
        pg.sprite.Sprite.__init__(self, *groups)
        self.slope = 0
        self.image = pg.image.load("data/shoot.png")
        self.image = pg.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()
        self.firstTime = True

        self.speed = 6.0

        if clock() > shoottime + 1:
            self.notShoot = False
            shoottime = clock() + 1
        else:
            self.notShoot = True
    def update(self):
        if self.notShoot:
            self.kill()
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
        pass"""