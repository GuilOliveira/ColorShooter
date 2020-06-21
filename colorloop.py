import random

r = 0
g = 0
b = 0
rCheck = True
gCheck = True
bCheck = True

def ColorLoop(r, g, b, rCheck, gCheck, bCheck):
    maxn = 11
    minn = 1
    if rCheck:
        r += random.randint(minn, maxn)
    else:
        r -= random.randint(minn, maxn)
    if gCheck:
        g += random.randint(minn, maxn)
    else:
        g -= random.randint(minn, maxn)
    if bCheck:
        b += random.randint(minn, maxn)
    else:
        b -= random.randint(minn, maxn)
    if r > 255:
        r = 255
        rCheck = False
    elif r < 0:
        r = 0
        rCheck = True
    if g > 255:
        g = 255
        gCheck = False
    elif g < 0:
        g = 0
        gCheck = True
    if b > 255:
        b = 255
        bCheck = False
    elif b < 0:
        b = 0
        bCheck = True
    return r, g, b, rCheck, gCheck, bCheck