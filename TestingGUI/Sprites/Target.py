from math import hypot

import pygame

from TestingGUI.Utils.Pathing.Path import dataProcessing
from TestingGUI.Utils.Utils import loadImage, getScreenDimensions


class Target(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.screen = screen
        self.coordinates = dataProcessing()
        self.image = loadImage('/home/tinku/Eye-Tracking-Disease-Detection/TestingGUI/Assets/target.png', 40)
        self.velocity = 5
        self.index = 0
        self.isMovementFinished = False
        self.rect = self.image.get_rect()
        self.rect.center = getScreenDimensions()

    def followPath(self, ticks):
        if self.isMovementFinished:
            self.index += 1
        print(self.coordinates[self.index])
        self.move(self.coordinates[self.index], ticks)

    def move(self, point, ticks):
        self.isMovementFinished = False
        rectList = list(self.rect.center)
        distX = point[0] - rectList[0]
        distY = point[1] - rectList[1]
        if distX < 0:
            rectList[0] -= float(self.velocity) * ticks / 1000
        if distY < 0:
            rectList[1] -= float(self.velocity) * ticks / 1000
        if distX > 0:  # Is broken
            rectList[0] += float(self.velocity) * ticks / 1000
        if distY > 0:  # Is broken
            rectList[1] += float(self.velocity) * ticks / 1000
        self.rect.center = tuple(rectList)
        constrainedRect = self.rect.clamp(self.screen.get_rect())
        self.rect = constrainedRect
        self.screen.blit(self.image, self.rect)
        if point == [0, 800] or point == [800, 0] or point == [0, 0] or point == [800, 800]:
            if hypot(point[0] - rectList[0], point[1] - rectList[1]) <= 30:
                print("True but is a corner")
                self.isMovementFinished = True
                return None
        elif hypot(point[0] - rectList[0], point[1] - rectList[1]) <= 1.5:
            print(True)
            self.isMovementFinished = True
            return None
