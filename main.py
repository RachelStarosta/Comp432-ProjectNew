"""
Drawing a simple game window
"""


import pygame as pg
from pygame.locals import *
#import time

if __name__ == "__main__":
    pg.init()
    surfaceSize = (500, 500)
    surface = pg.display.set_mode(surfaceSize)
    surface.fill((82, 15, 54))

    #To have a picture as a backgound:
    backG = pg.image.load("SampleBackground.png")
    backG = pg.transform.scale(backG, surfaceSize)
    surface.blit(backG, (0,0))

    pg.display.flip()

    #updates the full display, needed to see the changes

    """ Defining the Event Loop"""

    running  = True
# Establishes that pressing the escape key end running the game
# and the game window...
    while running:
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
