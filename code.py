# CircuitPlaygroundExpress_NeoPixel

import board
import neopixel
import time

RED = (0x10, 0, 0) # 0x100000 also works
YELLOW=(0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

#choose which demos to play
# 1 means play, 0 means don't!
simpleCircleDemo = 1
flashDemo = 0
rainbowDemo = 0
rainbowCycleDemo = 0

def blink():
    interval = 0.5
    colors = []

    for i in range(len(pixels)):
        colors.append(pixels[i])

    for i in range(len(pixels)):
        time.sleep(interval)

        for j in range(len(pixels)):
            #pixels[j] = BLACK
            pixels.fill(BLACK)
        time.sleep(interval/2)

        for j in range(len(pixels)):
            pixels[j] = colors[j]
        time.sleep(interval)

def chaseLights(iterations):
    interval = .2
    print("chaseLights");
    for i in range(len(pixels)):
        if i % 2:
            pixels[i] = GREEN
        else:
            pixels[i] = RED
    time.sleep(interval)

    for i in range(iterations):
        for j in range(len(pixels)):
            if pixels[j] == GREEN:
                pixels[j] = RED
            else:
                pixels[j] = GREEN
        time.sleep(interval)

def simpleCircle(iterations):
    print("simpleCircle")
    for i in range(iterations):
        if pixels[0] == RED:
            pixels.fill(GREEN)
        else:
            pixels.fill(RED)
        time.sleep(.4)

while True:
    chaseLights(30)
    simpleCircle(20)
