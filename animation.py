import pygame as pg, os

def clock():
    current_time = pg.time.get_ticks()
    return current_time

class Animation():
    def __init__(self):
        self.frameTime = clock()
        self.resetFrame = False
        self.frameCount = 1
        self.checker2 = 0
        self.frametime = clock()

    def animator(self, path, checker1, speed, time):
        if speed > 2:
            time = time * (1-((speed-2)/10))

        if self.checker2 == 0:
            self.checker2 = checker1
        if checker1 != self.checker2:
            self.frameCount = 1
            self.checker2 = checker1
        if speed < 0:
            speed *= -1
        self.maxFrames = len(os.listdir(path))
        if clock() >= self.frametime + time:
            if self.frameCount < self.maxFrames:
                self.frameCount += 1
            else:
                self.frameCount = 1
            self.frametime = clock() + time
        return path + str(self.frameCount) + ".png"
