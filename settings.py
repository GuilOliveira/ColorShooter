import pygame as pg

screenW = 900
screenH = 600
clock = pg.time.Clock()


def title():
    name = "{} - FPS: {:.2f}".format("Test Build - ColorShooter", clock.get_fps())
    return name


tilesize = 30
gridW = screenW / tilesize
gridH = screenH / tilesize
