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
    return None


def loadImage(pathToImage, size):
    surface = pygame.image.load(pathToImage).convert_alpha()
    return pygame.transform.scale(surface, [size, size])


def init():
    pygame.display.set_caption("Eye Calibration GUI")
    pygame.event.set_allowed([pygame.QUIT])
