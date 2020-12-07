import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.screen = screen
        self.screen.fill([0, 255, 0])

    def fill(self, color):
        self.screen.fill(color)
