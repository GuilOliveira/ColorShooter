import pygame as pg
import random, math
from settings import *
import animation

def checkCollision(sprite1, sprite2):
    collision = pg.sprite.collide_rect(sprite1, sprite2)
    return collision


def spawnEnemy(Width, Height):
    quadrant = random.randint(0, 3)

    if quadrant == 0:
        spawnCords = (random.randint(0, Width), -110)
    elif quadrant == 1:
        spawnCords = (-110, random.randint(0, Height))
    elif quadrant == 2:
        spawnCords = (random.randint(0, Width), Height+110)
    else:
        spawnCords = (Width+110, random.randint(0, Height))
    return spawnCords[0], spawnCords[1]


class SkeletonWarrior(pg.sprite.Sprite):
    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = pg.image.load("data/sprites/SkeletonWarrior/front/1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = spawnEnemy(screenW, screenH)
        self.xspeed = 0
        self.yspeed = 0
        self.speed = 2
        self.aniID = 0
        self.health = 100
        self.newAnimator = animation.Animation()
    def update(self, playerCords):
        player = pg.Vector2(playerCords)
        zombie = pg.Vector2(self.rect.center)
        movement = player - zombie
        if movement != (0, 0):
            movement.normalize()
            movement.scale_to_length(self.speed)
            self.rect.move_ip(movement)
        if movement[0] < 0 and (-0.36 < movement[1] < 0.36):
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/SidedR/", 2, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif movement[0] > 0 and (-0.36 < movement[1] < 0.36):
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/SidedL/", 3, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif (-0.36 < movement[0] < 0.36) and movement[1] >= 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/Front/", 3, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif (-0.36 < movement[0] < 0.36) and movement[1] < 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/Back/", 3, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif movement[0] < 0 and movement[1] > 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/FrontSidedR/", 2, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif movement[0] > 0 and movement[1] > 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/FrontSidedL/", 2, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif movement[0] < 0 and movement[1] < 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/BackSidedR/", 2, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()
        elif movement[0] > 0 and movement[1] < 0:
            self.frame = self.newAnimator.animator("data/sprites/SkeletonWarrior/BackSidedL/", 2, 2, 65)
            self.image = pg.image.load(self.frame).convert_alpha()

        #if checkCollision()

        if self.health <= 0:
            self.kill
