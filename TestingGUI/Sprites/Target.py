import pygame

from TestingGUI.Utils.Utils import loadImage


class Target(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.screen = screen
        self.image = loadImage('/home/tinku/Eye-Tracking-Disease-Detection/TestingGUI/Assets/target.png', 20)
        self.velocity = 5
        self.rect = self.image.get_rect()
        self.rect.center = [400, 400]

    def move(self, x, y, ticks):
        rectList = list(self.rect.center)
        if x < rectList[0]:
            rectList[0] -= float(self.velocity) * ticks / 1000
        if y < rectList[1]:
            rectList[1] -= float(self.velocity) * ticks / 1000
        if x > rectList[0]:
            rectList[0] += float(self.velocity) * ticks / 1000
        if y > rectList[1]:
            rectList[1] += float(self.velocity) * ticks / 1000
        self.rect.center = tuple(rectList)
        constrainedRect = self.rect.clamp(self.screen.get_rect())
        self.rect = constrainedRect
        self.screen.blit(self.image, self.rect)
        print(str(ticks) + ": " + str(self.rect.center))
