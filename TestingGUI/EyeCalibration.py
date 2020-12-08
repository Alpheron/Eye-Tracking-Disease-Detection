import pygame

from TestingGUI.Sprites.Background import Background
from TestingGUI.Sprites.Target import Target
from TestingGUI.Utils.Utils import getScreenDimensions, quitLoopConditional, init


class EyeCalibration:
    def __init__(self):
        self.screen = pygame.display.set_mode(getScreenDimensions())
        init()
        self.clock = pygame.time.Clock()
        self.background = Background(self.screen)
        self.target = Target(self.screen)
        self.isRunning = False
        pygame.init()
        self.calibrationRoutine()

    def calibrationRoutine(self):
        self.isRunning = True
        ticks = 0
        while self.isRunning:
            self.background.fill([0, 255, 0])
            self.target.followPath(ticks)
            ticks = self.clock.tick_busy_loop(60)
            pygame.display.flip()
            quitLoopConditional(self.isRunning)


if __name__ == '__main__':
    exception = EyeCalibration()
