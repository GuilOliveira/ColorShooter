import pygame as pg, os

global resetFrame
resetFrame = False
global frameCount
frameCount = 1
global checker2
checker2 = 0


def clock():
    current_time = pg.time.get_ticks()
    return current_time


global frameTime
class initFrameTime():
    def __init__(self):
        global frameTime
        frameTime = clock()
initFrameTime()


def Animation(path,checker1,speed):
    global frameCount
    global resetFrame
    global frameTime
    global checker2
    if checker2 == 0:
        checker2 = checker1
    if checker1 != checker2:
        frameCount = 1
        checker2 = checker1
    if speed < 0:
        speed *= -1
    newFrame = clock()
    maxFrames = len(os.listdir(path))
    actualFrame = path + str(frameCount) + ".png"
    if resetFrame == False:
        frameTime = newFrame + 28 - (speed / 2)
        resetFrame = True
    if newFrame - frameTime > 28 - (speed / 2):
        resetFrame = False
        if frameCount >= maxFrames:
            frameCount = 1
            actualFrame = path + str(frameCount) + ".png"
        else:
            frameCount += 1
            actualFrame = path + str(frameCount) + ".png"
    return actualFrame
