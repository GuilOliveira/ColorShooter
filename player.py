import pygame as pg
import animation

ScreenW = 1360
ScreenH = 765


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/Player/Front-Stopped/1.png").convert_alpha()
        self.image = pg.transform.scale(self.image, [80, 120])
        self.rect = self.image.get_rect()

        self.rect[0] = ScreenW / 2 - 40.0
        self.rect[1] = ScreenH / 2 - 60.0
        self.accel = 1
        self.xspeed = 0
        self.yspeed = 0
        self.maxSpeed = 3

        self.frontS = []
        self.cont = 1
        self.contString = ""
        self.running = False
        self.aniID = 0

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LSHIFT] or key[pg.K_RSHIFT]:
            self.maxSpeed = 1.4

        else:
            self.maxSpeed = 3
        if key[pg.K_w] or key[pg.K_UP]:
            if self.xspeed > -self.maxSpeed:
                self.xspeed -= self.accel
            else:
                self.xspeed = -self.maxSpeed
        if key[pg.K_s] or key[pg.K_DOWN]:
            if self.xspeed < self.maxSpeed:
                self.xspeed += self.accel
            else:
                self.xspeed = self.maxSpeed
        if ((not key[pg.K_w] and not key[pg.K_UP]) and (not key[pg.K_s] and not key[pg.K_DOWN])) or ((key[pg.K_w] or key[pg.K_UP]) and (key[pg.K_s] or key[pg.K_DOWN])):
            self.xspeed /= 1.5
            if -0.5 < self.xspeed < 0.5:
                self.xspeed = 0

        if key[pg.K_a] or key[pg.K_LEFT]:
            if self.yspeed > -self.maxSpeed:
                self.yspeed -= self.accel
            else:
                self.yspeed = -self.maxSpeed
        if key[pg.K_d] or key[pg.K_RIGHT]:
            if self.yspeed < self.maxSpeed:
                self.yspeed += self.accel
            else:
                self.yspeed = self.maxSpeed
        if ((not key[pg.K_a] and not key[pg.K_LEFT]) and (not key[pg.K_d] and not key[pg.K_RIGHT])) or ((key[pg.K_a] or key[pg.K_LEFT]) and (key[pg.K_d] or key[pg.K_RIGHT])):
            self.yspeed /= 1.5
            if -0.5 < self.yspeed < 0.5:
                self.yspeed = 0
        self.rect[1] += self.xspeed
        self.rect[0] += self.yspeed

        if self.xspeed > 0 and self.yspeed == 0:
            self.frame = animation.Animation("data/sprites/Player/Front-Running/", 2, self.xspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 1

        if self.xspeed < 0 and self.yspeed == 0:
            self.frame = animation.Animation("data/sprites/Player/Back-Running/", 3, self.xspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 2

        if self.xspeed == 0 and self.yspeed < 0:
            self.frame = animation.Animation("data/sprites/Player/SidedL-Running/", 4, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 3

        if self.xspeed == 0 and self.yspeed > 0:
            self.frame = animation.Animation("data/sprites/Player/SidedR-Running/", 5, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 4

        if self.xspeed > 0 and self.yspeed > 0:
            self.frame = animation.Animation("data/sprites/Player/FrontR-Running/", 6, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 5

        if self.xspeed < 0 and self.yspeed > 0:
            self.frame = animation.Animation("data/sprites/Player/BackSidedR-Running/", 7, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 6

        if self.xspeed < 0 and self.yspeed < 0:
            self.frame = animation.Animation("data/sprites/Player/BackSidedL-Running/", 8, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 7

        if self.xspeed > 0 and self.yspeed < 0:
            self.frame = animation.Animation("data/sprites/Player/FrontSideL-Running/", 9, self.yspeed)
            self.image = pg.image.load(self.frame).convert_alpha()
            #self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 8

        if self.xspeed == 0 and self.yspeed == 0:
            if self.aniID == 1:
                self.frame = animation.Animation("data/sprites/Player/Front-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 2:
                self.frame = animation.Animation("data/sprites/Player/Back-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 3:
                self.frame = animation.Animation("data/sprites/Player/LSided-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 4:
                self.frame = animation.Animation("data/sprites/Player/SidedR-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
                pass
            if self.aniID == 5:
                self.frame = animation.Animation("data/sprites/Player/FrontSidedR-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 6:
                self.frame = animation.Animation("data/sprites/Player/BackSidedR-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 7:
                self.frame = animation.Animation("data/sprites/Player/BackSidedL-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 8:
                self.frame = animation.Animation("data/sprites/Player/FrontSidedL-Stopped/", 1, 7)
                self.image = pg.image.load(self.frame).convert_alpha()
                #self.image = pg.transform.scale(self.image, [80, 120])