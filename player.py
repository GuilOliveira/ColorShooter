import pygame as pg
import animation
from settings import *


def clock():
    current_time = pg.time.get_ticks()
    return current_time

global runTime
runTime = clock()

global ufoMove
ufoMove = clock()


class Ufo(pg.sprite.Sprite):
    def __init__(self):
        global ufoMove
        #region ----UFO Variables
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("data/sprites/Ufo/ufo.png").convert_alpha()
        self.image = pg.transform.scale(self.image, [33, 33])
        self.rect = self.image.get_rect()
        self.cont = 0
        self.upping = True

        if clock() > ufoMove + 500:
            self.moveColldown = False
            ufoMove = clock() + 500
        else:
            self.moveColldown = True
        #endregion
    def update(self):
        #region ----UFO Movimentations
        if self.moveColldown:
            pass
        else:
            if self.upping:
                if self.cont == 40:
                    self.upping = False
                    self.cont -= 1
                else:
                    self.rect[1] -= 1
                    self.cont += 1
            else:
                if self.cont == 0:
                    self.upping = True
                    self.cont += 1
                else:
                    self.rect[1] += 1
                    self.cont -= 1
        #endregion

class Player(pg.sprite.Sprite):

    def __init__(self):
        #region ----Player Variables
        pg.sprite.Sprite.__init__(self)
        self.PlayerAnimator = animation.Animation()
        self.image = pg.image.load("data/sprites/Player/Front-Stopped/1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = screenW / 2 - 20.0
        self.rect[1] = screenH / 2 - 30.0
        self.accel = 1
        self.xspeed = 0
        self.yspeed = 0
        self.maxSpeed = 3

        self.cont = 1
        self.running = False
        self.aniID = 0

        self.maxHealth = 200
        self.health = 200
        self.coins = 0
        self.maxStamina = 150
        self.stamina = 0
        self.staminaCD = False
        self.staminaRestore = True
        self.staminaWait = False
        #endregion
    def update(self):
        global runTime
        key = pg.key.get_pressed()
        #region ----Stamina Stats
        if key[pg.K_LSHIFT] or key[pg.K_RSHIFT]:
            self.staminaRestore = False
            runTime = clock() + 500
            if self.stamina <= 0:
                if not self.staminaWait:
                    self.staminaCD = True
                    self.maxSpeed = 2
                    self.staminaWait = True
            else:
                self.maxSpeed = 4
                self.stamina -= 1.5
        else:
            self.maxSpeed = 2
        if self.staminaCD:
            if clock() > runTime + 500:
                self.staminaRestore = True
                self.staminaWait = False
        if self.staminaRestore:
            if self.stamina >= self.maxStamina:
                self.stamina = self.maxStamina
                self.staminaRestore = False
            else:
                self.stamina += 1
        #endregion
        #region ----Player Movimentation
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
        if ((not key[pg.K_w] and not key[pg.K_UP]) and (not key[pg.K_s] and not key[pg.K_DOWN])) or (
                (key[pg.K_w] or key[pg.K_UP]) and (key[pg.K_s] or key[pg.K_DOWN])):
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
        if ((not key[pg.K_a] and not key[pg.K_LEFT]) and (not key[pg.K_d] and not key[pg.K_RIGHT])) or (
                (key[pg.K_a] or key[pg.K_LEFT]) and (key[pg.K_d] or key[pg.K_RIGHT])):
            self.yspeed = 0

        self.rect[1] += self.xspeed
        self.rect[0] += self.yspeed
        #endregion
        #region ----Player Animation
        if self.xspeed > 0 and self.yspeed == 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/Front-Running/", 2, self.maxSpeed, 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 1

        if self.xspeed < 0 and self.yspeed == 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/Back-Running/", 3, self.maxSpeed, 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 2

        if self.xspeed == 0 and self.yspeed < 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/SidedL-Running/", 4, self.maxSpeed, 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 3

        if self.xspeed == 0 and self.yspeed > 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/SidedR-Running/", 5, self.maxSpeed, 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 4

        if self.xspeed > 0 and self.yspeed > 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/FrontR-Running/", 6, self.maxSpeed , 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 5

        if self.xspeed < 0 and self.yspeed > 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/BackSidedR-Running/", 7, self.maxSpeed , 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 6

        if self.xspeed < 0 and self.yspeed < 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/BackSidedL-Running/", 8, self.maxSpeed , 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 7

        if self.xspeed > 0 and self.yspeed < 0:
            self.frame = self.PlayerAnimator.animator("data/sprites/Player/FrontSideL-Running/", 9, self.maxSpeed , 28)
            self.image = pg.image.load(self.frame).convert_alpha()
            # self.image = pg.transform.scale(self.image, [80, 120])
            self.aniID = 8

        if self.xspeed == 0 and self.yspeed == 0:
            if self.aniID == 1:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/Front-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 2:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/Back-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 3:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/LSided-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 4:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/SidedR-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
                pass
            if self.aniID == 5:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/FrontSidedR-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 6:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/BackSidedR-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 7:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/BackSidedL-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
            if self.aniID == 8:
                self.frame = self.PlayerAnimator.animator("data/sprites/Player/FrontSidedL-Stopped/", 1, self.maxSpeed, 28)
                self.image = pg.image.load(self.frame).convert_alpha()
                # self.image = pg.transform.scale(self.image, [80, 120])
        #endregion