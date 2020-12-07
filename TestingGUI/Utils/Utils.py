import sys

import pygame


def getScreenDimensions():
    width = 800
    height = 800
    return [width, height]


def quitLoopConditional(started):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            started = False
            pygame.quit()
            sys.exit()
    return None


def loadImage(pathToImage, size):
    surface = pygame.image.load(pathToImage).convert_alpha()
    return pygame.transform.scale(surface, [size, size])
