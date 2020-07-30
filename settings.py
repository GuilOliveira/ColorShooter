import pygame as pg

screenW = 1200
screenH = 800
clock = pg.time.Clock()


def title():
    name = "{} - FPS: {:.2f}".format("Test Build - ColorShooter", clock.get_fps())
    return name


tilesize = 30
gridW = screenW / tilesize
gridH = screenH / tilesize
